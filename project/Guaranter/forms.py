from django import forms
from .models import Guaranter

class GuranterForm(forms.ModelForm):
    class Meta:
        model = Guaranter
        fields = '__all__'


