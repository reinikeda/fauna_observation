from django.urls import path
from . import views

urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('animal_classes/', views.AnimalClassListView.as_view(), name='all_classes'),
     path('animal_classes/<int:pk>/', views.AnimalSpeciesListView.as_view(), name='species_list'),
     path('species/<int:pk>/', views.AnimalSpeciesDetailView.as_view(), name='species_detail'),
     path('observations/', views.ObservationListView.as_view(), name='observations'),
     path('animals_data/', views.DataAnalysisView.as_view(), name='data_analysis'),
     path('about/', views.AboutView.as_view(), name='about'),
     path('add_observation/', views.add_observation, name='add_observation'),
     path('edit_observation/<int:pk>/', views.edit_observation, name='edit_observation'),
     path('delete_observation/<int:pk>/', views.delete_observation, name='delete_observation'),
     path('my_observations/', views.UserObservationListView.as_view(), name='user_observations'),
]
