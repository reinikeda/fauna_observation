from PIL import Image
from datetime import date
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class AnimalClass(models.Model):
    class_scientific = models.CharField(_('class scientific name'), max_length=200, null=False, blank=False)
    class_en = models.CharField(_('class english name'), max_length=200, null=False, blank=False)
    class_national = models.CharField(_('class national name'), max_length=200, null=False, blank=False)
    example_image = models.ImageField(_('example image'), upload_to='faunaweb/classes/', null=True, blank=True)

    def __str__(self):
        return f'{self.class_scientific} ({self.class_national})'
    
    class Meta:
        ordering = ['class_scientific']
        verbose_name = _('animal class')
        verbose_name_plural = _('animal classes')


class AnimalSpecies(models.Model):
    class_id = models.ForeignKey(
        AnimalClass,
        on_delete=models.PROTECT,
        related_name='species',
        to_field='id',
        verbose_name=_('animal classes')
    )
    order_scientific = models.CharField(_('order scientific name'), max_length=200, null=False, blank=False)
    order_national = models.CharField(_('order national name'), max_length=200, null=True, blank=True)
    family_scientific = models.CharField(_('family scientific name'), max_length=200, null=False, blank=False)
    family_national = models.CharField(_('order national name'), max_length=200, null=True, blank=True)
    species_scientific = models.CharField(_('species scientific name'), max_length=200, null=False, blank=False)
    species_en = models.CharField(_('species english name'), max_length=200, null=True, blank=True)
    species_national = models.CharField(_('species national name'), max_length=200, null=True, blank=True)
    endangered = models.BooleanField(_('endangered species'), default=False)
    species_image = models.ImageField(_('species image'), upload_to='faunaweb/species/', null=True, blank=True)

    def __str__(self):
        return f'{self.class_id} - {self.order_scientific}: {self.species_scientific} ({self.species_national})'
    
    class Meta:
        ordering = ['order_scientific', 'species_scientific']


class Place(models.Model):
    place_en = models.CharField(_('place english name'), max_length=200, null=True, blank=True)
    place_national = models.CharField(_('place national name'), max_length=200, null=False, blank=False)

    def __str__(self):
        return f'{self.place_national}'

    class Meta:
        ordering = ['place_national']
        verbose_name = _('place')
        verbose_name_plural = _('places')


class Observation(models.Model):
    species = models.ForeignKey(
        AnimalSpecies,
        on_delete=models.PROTECT,
        related_name='observation',
        verbose_name=_('animal species')
    )
    date = models.DateField(_('date'), auto_now_add=False, default=date.today)
    count = models.IntegerField(_('count'), default=1)
    place = models.ForeignKey(
        Place,
        on_delete=models.PROTECT,
        related_name='observation',
        verbose_name=_('place')
    )
    observer = models.ForeignKey(
        User,
        verbose_name=_('observer'),
        on_delete=models.SET_NULL,
        related_name='observation',
        null=True, blank=True
    )
    photo = models.ImageField(
        _('photo'),
        upload_to='user_profile/observations',
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.date} - {self.species} ({self.observer})'
    
    class Meta:
        ordering = ['-date']
        verbose_name=_('observation')
        verbose_name_plural=_('observations')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        photo = Image.open(self.photo.path)
        if photo.height > 400 or photo.width > 400:
            output_size = (400, 400)
            photo.thumbnail(output_size)
            photo.save(self.photo.path)
            print('photo resized')