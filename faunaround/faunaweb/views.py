from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import generic
from django.utils.translation import gettext_lazy as _
from . import models
from .forms import NewObservationForm

def index(request):
    return render(request, 'faunaweb/index.html')

def about(request):
    return render(request, 'faunaweb/about.html')

class AnimalClassListView(generic.ListView):
    model = models.AnimalClass
    template_name = 'faunaweb/animal_classes.html'


class AnimalSpeciesListView(generic.ListView):
    model = models.AnimalSpecies
    paginate_by = 12
    template_name = 'faunaweb/species_list.html'
    context_object_name = 'species_list'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(class_id=self.kwargs['pk'])
        query = self.request.GET.get('search')
        if query:
            qs = qs.filter(
            Q(species_scientific__icontains=query) |
            Q(species_en__icontains=query) |
            Q(species_national__icontains=query)
    )
        return qs


class AnimalSpeciesDetailView(generic.DetailView):
    model = models.AnimalSpecies
    template_name = 'faunaweb/species_detail.html'


class ObservationListView(generic.ListView):
    model = models.Observation
    template_name = 'faunaweb/observation.html'


@login_required
def add_observation(request):
    if request.method == 'POST':
        form = NewObservationForm(request.POST, request.FILES)
        if form.is_valid():
            observation = form.save(commit=False)
            observation.observer = request.user
            observation.save()
            return redirect('observations')
    else:
        form = NewObservationForm()
    return render(request, 'faunaweb/add_observation.html', {'form': form})