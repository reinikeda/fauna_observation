from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AnimalResource(resources.ModelResource):
    model = models.AnimalClass


class AnimalClassAdmin(ImportExportModelAdmin):
    resource_class = AnimalResource
    list_display = ('class_scientific', 'class_en', 'class_national')


class BaseClassAdmin(ImportExportModelAdmin):
    resource_class = None
    list_display = ('class_id', 'order_scientific', 'order_national', 'family_scientific', 'family_national', 'species_scientific', 'species_en', 'species_national', 'endangered', )
    list_display_links = ('species_scientific', )
    list_filter = ('order_scientific', 'family_scientific', 'endangered', )
    search_fields = ('species_scientific', 'species_en', 'species_national', )
    fieldsets = (
        (_('Class'), {'fields': ('class_id', )}),
        (_('Order'), {'fields': ('order_scientific', 'order_national')}),
        (_('Family'), {'fields': ('family_scientific', 'family_national')}),
        (_('Species'), {'fields': ('species_scientific', 'species_en', 'species_national')}),
        (_('Endangered'), {'fields': ('endangered', )}),
        (_('Image'), {'fields': ('species_image', )})
    )

class MammalsRecource(BaseClassAdmin):
    resource_class = resources.ModelResource
    model = models.Mammals


class BirdsRecource(BaseClassAdmin):
    resource_class = resources.ModelResource
    model = models.Birds


class RayfinnedFishesRecource(BaseClassAdmin):
    resource_class = resources.ModelResource
    model = models.RayfinnedFishes


class ReptilesRecource(BaseClassAdmin):
    resource_class = resources.ModelResource
    model = models.Reptiles


class AmphibiansRecource(BaseClassAdmin):
    resource_class = resources.ModelResource
    model = models.Amphibians


class MalacostracansRecource(BaseClassAdmin):
    resource_class = resources.ModelResource
    model = models.Malacostracans


class InsectsRecource(BaseClassAdmin):
    resource_class = resources.ModelResource
    model = models.Insects


class ArachnidsRecource(BaseClassAdmin):
    resource_class = resources.ModelResource
    model = models.Arachnids


class PlaceResource(resources.ModelResource):
    model = models.Place

class PlaceAdmin(ImportExportModelAdmin):
    resource_class = PlaceResource
    list_display = ('place_en', 'place_national')
    list_display_links = ('place_national', )
    search_fields = ('place_en', 'place_national', )


admin.site.register(models.AnimalClass, AnimalClassAdmin)
admin.site.register(models.Mammals, BaseClassAdmin)
admin.site.register(models.Birds, BaseClassAdmin)
admin.site.register(models.RayfinnedFishes, BaseClassAdmin)
admin.site.register(models.Reptiles, BaseClassAdmin)
admin.site.register(models.Amphibians, BaseClassAdmin)
admin.site.register(models.Malacostracans, BaseClassAdmin)
admin.site.register(models.Insects, BaseClassAdmin)
admin.site.register(models.Arachnids, BaseClassAdmin)
admin.site.register(models.Place, PlaceAdmin)