from django.db.models import Q
from django.core.paginator import Paginator
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
            qs = models.Mammals.objects.all()
        elif class_type == 'birds':
            qs = models.Birds.objects.all()
        elif class_type == 'rayfinnedfishes':
            qs = models.RayfinnedFishes.objects.all()
        elif class_type == 'reptiles':
            qs = models.Reptiles.objects.all()
        elif class_type == 'amphibians':
            qs = models.Amphibians.objects.all()
        elif class_type == 'malacostracans':
            qs = models.Malacostracans.objects.all()
        elif class_type == 'insects':
            qs = models.Insects.objects.all()
        elif class_type == 'arachnids':
            qs = models.Arachnids.objects.all()
        else:
            qs = models.Animal.objects.none()
        query = self.request.GET.get('search')
        if query:
            qs = qs.filter(
                Q(species_scientific__icontains=query) |
                Q(species_en__icontains=query) |
                Q(species_national__icontains=query)
            )
        return qs