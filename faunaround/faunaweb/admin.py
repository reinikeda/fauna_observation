from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models
from import_export.admin import ImportExportModelAdmin


class AnimalClassAdmin(ImportExportModelAdmin):
    list_display = ('class_scientific', 'class_en', 'class_national')


class AnimalSpeciesAdmin(ImportExportModelAdmin):
    list_display = ('class_id', 'order_scientific', 'order_national', 'family_scientific', 'family_national', 'species_scientific', 'species_en', 'species_national', 'endangered', )
    list_display_links = ('species_scientific', )
    list_filter = ('class_id', 'endangered', )
    search_fields = ('species_scientific', 'species_en', 'species_national', )
    fieldsets = (
        (_('Class'), {'fields': ('class_id', )}),
        (_('Order'), {'fields': ('order_scientific', 'order_national')}),
        (_('Family'), {'fields': ('family_scientific', 'family_national')}),
        (_('Species'), {'fields': ('species_scientific', 'species_en', 'species_national')}),
        (_('Endangered'), {'fields': ('endangered', )}),
        (_('Image'), {'fields': ('species_image', )})
    )


class PlaceAdmin(ImportExportModelAdmin):
    list_display = ('place_en', 'place_national')
    list_display_links = ('place_national', )
    search_fields = ('place_en', 'place_national', )


admin.site.register(models.AnimalClass, AnimalClassAdmin)
admin.site.register(models.AnimalSpecies, AnimalSpeciesAdmin)
admin.site.register(models.Place, PlaceAdmin)
admin.site.register(models.Observation)
admin.site.register(models.Content)