from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.shortcuts import render, redirect
from django.views import generic
from django.utils.translation import gettext_lazy as _
import requests
from bs4 import BeautifulSoup
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        species = self.object
        url = 'https://en.wikipedia.org/wiki/' + species.species_en.replace(' ', '_')
        response = requests.get(url=url)
        soup = BeautifulSoup(response.content, 'html.parser')
        p_tags = soup.find_all('p')
        intro = '\n<br><br>\n'.join([p.get_text() for p in p_tags[:4] if p.get_text().strip()])
        if not intro:
            intro = "No species info yet"
        count = species.observation.aggregate(Sum('count'))['count__sum']
        context['observation_count'] = count or 0
        context['intro'] = intro
        context['wikipedia_url'] = url
        return context

class ObservationListView(generic.ListView):
    model = models.Observation
    template_name = 'faunaweb/observation.html'


class UserObservationListView(generic.ListView):
    model = models.Observation
    template_name = 'faunaweb/user_observation.html'
    context_object_name = 'user_observation_list'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(observer=self.request.user)


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