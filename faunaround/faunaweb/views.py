from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils.translation import gettext_lazy as _
from . import models

def index(request):
    return render(request, 'faunaweb/index.html')