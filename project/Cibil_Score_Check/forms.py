from django import forms
from .models import CibilScoreCheck

class CibilForms(forms.ModelForm):
    class Meta:
        model = CibilScoreCheck
        fields = '__all__'