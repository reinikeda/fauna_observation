from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from . import models

def index(request):
    return render(request, 'faunaweb/index.html')

def about(request):
    return render(request, 'faunaweb/about.html')

class AnimalClassListView(generic.ListView):
    model = models.AnimalClass
    template_name = 'faunaweb/animal_classes.html'


class SpeciesListView(generic.ListView):
    model = models.Animal
    paginate_by = 12
    template_name = 'faunaweb/species_list.html'

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
    

class SpeciesDetailView(generic.DetailView):
    template_name = 'faunaweb/species_detail.html'

    def get_object(self, queryset=None):
        model_name = self.kwargs.get('model_name')
        model_map = {
            'mammals': models.Mammals,
            'birds': models.Birds,
            'rayfinnedfishes': models.RayfinnedFishes,
            'reptiles': models.Reptiles,
            'amphibians': models.Amphibians,
            'malacostracans': models.Malacostracans,
            'insects': models.Insects,
            'arachnids': models.Arachnids,
        }
        model_class = model_map.get(model_name)

        if model_class is None:
            raise Http404("Invalid model name")
        return get_object_or_404(model_class, pk=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model_name']
        return context