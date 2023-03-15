from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('animal_classes/', views.AnimalClassListView.as_view(), name='all_classes'),
     path('animal_classes/<int:pk>/', views.AnimalSpeciesListView.as_view(), name='species_list'),
     path('species/<int:pk>/', views.AnimalSpeciesDetailView.as_view(), name='species_detail'),
     path('observations/', views.ObservationListView.as_view(), name='observations'),
     path('about/', views.about, name='about'),
]
