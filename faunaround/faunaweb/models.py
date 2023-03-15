from datetime import date
from PIL import Image
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


class Animal(models.Model):
    class_id = models.ForeignKey(
        'AnimalClass',
        on_delete=models.PROTECT,
        related_name='%(class)s',
        to_field='id',
        verbose_name=_('animal class')
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
        return f'{self.order_scientific}: {self.species_scientific} ({self.species_national})'
    
    class Meta:
        abstract = True
        ordering = ['order_scientific', 'species_scientific']

    def get_model_name(self):
        return self.__class__.__name__.lower()

class Mammals(Animal):
    class Meta:
        verbose_name = _('mammals species')
        verbose_name_plural = _('mammals species')


class Birds(Animal):
    class Meta:
        verbose_name = _('birds species')
        verbose_name_plural = _('birds species')


class RayfinnedFishes(Animal):
    class Meta:
        verbose_name = _('ray-finned fishes species')
        verbose_name_plural = _('ray-finned fishes species')


class Reptiles(Animal):
    class Meta:
        verbose_name = _('reptiles species')
        verbose_name_plural = _('reptiles species')


class Amphibians(Animal):
    class Meta:
        verbose_name = _('amphibians species')
        verbose_name_plural = _('amphibians species')


class Malacostracans(Animal):
    class Meta:
        verbose_name = _('malacostracans species')
        verbose_name_plural = _('malacostracans species')


class Insects(Animal):
    class Meta:
        verbose_name = _('insects species')
        verbose_name_plural = _('insects species')


class Arachnids(Animal):
    class Meta:
        verbose_name = _('arachnids species')
        verbose_name_plural = _('arachnids species')


class Place(models.Model):
    place_en = models.CharField(_('place english name'), max_length=200, null=True, blank=True)
    place_national = models.CharField(_('place national name'), max_length=200, null=False, blank=False)

    def __str__(self):
        return f'{self.place_national}'

    class Meta:
        ordering = ['place_national']
        verbose_name = _('place')
        verbose_name_plural = _('places')
