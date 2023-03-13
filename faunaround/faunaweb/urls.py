from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('animal_classes/', views.AnimalClassView.as_view(), name='animals'),
     path('mammals/', views.MammalsView.as_view(), name='mammals'),
     path('birds/', views.BirdsView.as_view(), name='birds'),
     path('rayfinnedfishes/', views.RayfinnedFishesView.as_view(), name='rayfinnedfishes'),
     path('reptiles/', views.ReptilesView.as_view(), name='reptiles'),
     path('amphibians/', views.AmphibiansView.as_view(), name='amphibians'),
     path('malacostracans/', views.MalacostracansView.as_view(), name='malacostracans'),
     path('insects/', views.InsectsView.as_view(), name='insects'),
     path('arachnids/', views.ArachnidsView.as_view(), name='arachnids'),
]
