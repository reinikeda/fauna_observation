from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('animal_classes/', views.AnimalClassListView.as_view(), name='all_classes'),
     path('animal_classes/<str:class_type>/', views.SpeciesListView.as_view(), name='species_list'),
     path('<str:model_name>/<int:pk>/', views.SpeciesDetailView.as_view(), name='species_detail'),
]
