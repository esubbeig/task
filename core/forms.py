from django import forms

from .models import *

# Defining form to handle add data
class DataCreationForm(forms.ModelForm):
    class Meta:
        model = DataResult
        fields = '__all__'
