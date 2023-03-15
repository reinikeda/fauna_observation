from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('my/', views.detail_active, name='profile_detail_active'),
    path('update/', views.update, name='profile_update'),
    path('<str:username>/', views.detail, name='profile_detail'),
]
