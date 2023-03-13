import csv
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils.translation import gettext_lazy as _
from . import models

def index(request):
    return render(request, 'faunaweb/index.html')

class AnimalClassView(generic.ListView):
    model = models.AnimalClass
    template_name = 'faunaweb/animal_classes.html'


class MammalsView(generic.ListView):
    model = models.Mammals
    paginate_by = 12
    template_name = 'faunaweb/mammals.html'


class BirdsView(generic.ListView):
    model = models.Birds
    paginate_by = 12
    template_name = 'faunaweb/birds.html'


class RayfinnedFishesView(generic.ListView):
    model = models.RayfinnedFishes
    paginate_by = 12
    template_name = 'faunaweb/rayfinnedfishes.html'


class ReptilesView(generic.ListView):
    model = models.Reptiles
    paginate_by = 12
    template_name = 'faunaweb/reptiles.html'


class AmphibiansView(generic.ListView):
    model = models.Amphibians
    paginate_by = 12
    template_name = 'faunaweb/amphibians.html'


class MalacostracansView(generic.ListView):
    model = models.Malacostracans
    paginate_by = 12
    template_name = 'faunaweb/malacostracans.html'


class InsectsView(generic.ListView):
    model = models.Insects
    paginate_by = 12
    template_name = 'faunaweb/insects.html'


class ArachnidsView(generic.ListView):
    model = models.Arachnids
    paginate_by = 12
    template_name = 'faunaweb/arachnids.html'