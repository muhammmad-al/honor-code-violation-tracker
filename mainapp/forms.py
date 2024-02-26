from django import forms
from .models import HonorCodeViolation

class HonorCodeViolationForm(forms.ModelForm):
    class Meta:
        model = HonorCodeViolation
        fields = ['name', 'date_of_incident', 'description', 'photo']