from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.utils import timezone
from django_select2.forms import Select2Widget
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
            'species': Select2Widget(),
            'place': Select2Widget(),
        }