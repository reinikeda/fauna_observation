from django import forms
from .models import Observation


class NewObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['date', 'species', 'count', 'place', 'photo']

class EditObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['date', 'species', 'count', 'place', 'photo']