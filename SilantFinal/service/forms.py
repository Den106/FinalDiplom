from django import forms
from .models import *

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'
        widgets ={
            'type': forms.RadioSelect()
        }

class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = '__all__'
