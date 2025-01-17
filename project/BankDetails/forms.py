from django import forms
from .models import BankDetails

class BankDetailsForm(forms.ModelForm):
    class Meta:
        model = BankDetails
        fields = '__all__'