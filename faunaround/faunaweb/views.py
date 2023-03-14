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


class OneClassView(generic.ListView):
    model = models.Animal
    paginate_by = 12
    template_name = 'faunaweb/one_class.html'

    def get_queryset(self):
        class_type = self.kwargs['class_type']
        if class_type == 'mammals':
            return models.Mammals.objects.all()
        elif class_type == 'birds':
            return models.Birds.objects.all()
        elif class_type == 'rayfinnedfishes':
            return models.RayfinnedFishes.objects.all()
        elif class_type == 'reptiles':
            return models.Reptiles.objects.all()
        elif class_type == 'amphibians':
            return models.Amphibians.objects.all()
        elif class_type == 'malacostracans':
            return models.Malacostracans.objects.all()
        elif class_type == 'insects':
            return models.Insects.objects.all()
        elif class_type == 'arachnids':
            return models.Arachnids.objects.all()
        else:
            return models.Animal.objects.none()