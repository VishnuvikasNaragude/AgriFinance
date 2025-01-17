from django import forms
from .models import Enquiry



class EnquriForms(forms.ModelForm):
    class Meta:
        model = Enquiry  # Replace with the correct model class
        fields = '__all__'