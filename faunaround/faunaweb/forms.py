from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.utils import timezone
from django import forms
from .models import Observation


class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['date', 'species', 'count', 'place', 'photo']
        widgets = {
            'date': DatePickerInput(
                attrs={
                    'name': 'date',
                },
                options={
                    'maxDate': timezone.now().strftime('%Y-%m-%d'),
                }),
        }