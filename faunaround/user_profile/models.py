from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image, ExifTags

class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), 
        verbose_name=_('user'), 
        on_delete=models.CASCADE,
        related_name='profile',
        unique=True,
    )
    photo = models.ImageField(
        _('photo'), 
        upload_to='user_profile/photos/',
        default='user_profile/photos/default.png',
    )

    def __str__(self) -> str:
        return str(self.user)
    
    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            photo = Image.open(self.photo.path)
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            try:
                exif = dict(photo._getexif().items())
                if exif[orientation] == 3:
                    photo = photo.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    photo = photo.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    photo = photo.rotate(90, expand=True)
            except (AttributeError, KeyError, IndexError):
                pass
            if photo.height > 400 or photo.width > 400:
                output_size = (400, 400)
                photo.thumbnail(output_size)
            photo.save(self.photo.path)