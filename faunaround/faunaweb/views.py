from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.utils.translation import gettext_lazy as _
import requests
import random
from bs4 import BeautifulSoup
from . import models
from .forms import ObservationForm


def about(request):
    return render(request, 'faunaweb/about.html')

class IndexView(generic.TemplateView):
    template_name = 'faunaweb/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_observations = models.Observation.objects.order_by('-date')[:7]
        top_species = models.Observation.objects.select_related('species').values('species', 'species__pk', 'species__species_national', 'species__species_scientific').annotate(species_count=Count('species')).order_by('-species_count')[:7]
        species_count = models.AnimalSpecies.objects.count()
        random_index = random.randint(0, species_count - 1)
        random_species = models.AnimalSpecies.objects.all()[random_index]
        context['latest_observations'] = latest_observations
        context['top_species'] = top_species
        context['random_species'] = random_species
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_animal_class = models.AnimalClass.objects.get(pk=self.kwargs['pk'])
        context['current_animal_class'] = current_animal_class
        return context

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
    paginate_by = 20
    template_name = 'faunaweb/observation.html'

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            qs = qs.filter(
            Q(species__species_scientific__icontains=query) |
            Q(species__species_en__icontains=query) |
            Q(species__species_national__icontains=query) |
            Q(place__place_national__icontains=query) |
            Q(date__icontains=query)
        )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        species_count = models.Observation.objects.values('species').distinct().count()
        total_species_count = models.AnimalSpecies.objects.count()
        entries_count = models.Observation.objects.count()
        context['species_count'] = species_count
        context['total_species_count'] = total_species_count
        context['entries_count'] = entries_count
        return context

    
class UserObservationListView(generic.ListView):
    model = models.Observation
    paginate_by = 20
    template_name = 'faunaweb/user_observation.html'
    context_object_name = 'user_observation_list'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(observer=self.request.user)
        query = self.request.GET.get('search')
        if query:
            qs = qs.filter(
            Q(species__species_scientific__icontains=query) |
            Q(species__species_en__icontains=query) |
            Q(species__species_national__icontains=query) |
            Q(place__place_national__icontains=query) |
            Q(date__icontains=query)
        )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        species_count = models.Observation.objects.filter(observer=user).values('species').distinct().count()
        total_species_count = models.AnimalSpecies.objects.count()
        entries_count = models.Observation.objects.filter(observer=user).count()
        context['species_count'] = species_count
        context['total_species_count'] = total_species_count
        context['entries_count'] = entries_count
        return context

@login_required
def add_observation(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST, request.FILES)
        if form.is_valid():
            observation = form.save(commit=False)
            observation.observer = request.user
            observation.save()
            return redirect('observations')
    else:
        form = ObservationForm()
    return render(request, 'faunaweb/add_observation.html', {'form': form})

@login_required
def edit_observation(request, pk):
    observation = get_object_or_404(models.Observation, pk=pk)
    if request.method == 'POST':
        form = ObservationForm(request.POST, request.FILES, instance=observation)
        if form.is_valid():
            observation = form.save(commit=False)
            observation.observer = request.user
            observation.save()
            return redirect('user_observations')
    else:
        form = ObservationForm(instance=observation)
    return render(request, 'faunaweb/edit_observation.html', {'form': form})

@login_required
def delete_observation(request, pk):
    observation = get_object_or_404(models.Observation, pk=pk)
    if request.method == 'POST':
        observation.delete()
        return redirect('user_observations')
    return render(request, 'faunaweb/delete_observation.html', {'observation': observation})