from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('animal_classes/', views.AnimalClassView.as_view(), name='animals'),
     path('animal_classes/<str:class_type>/', views.OneClassView.as_view(), name='one_class'),
]
