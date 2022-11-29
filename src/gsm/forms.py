from django import forms
from .models import Location, Signal

class signalForm(forms.ModelForm):
    class Meta:
        model = Signal
        fields = ['location']