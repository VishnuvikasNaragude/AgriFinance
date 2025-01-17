from django import forms
from .models import DocumentDetails

class DocumentDetailsForm(forms.ModelForm):
    class Meta:
        model = DocumentDetails
        fields = '__all__'