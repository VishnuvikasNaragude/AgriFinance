from django import forms
from .models import PreviousLoan

class PreviousLoanForm(forms.ModelForm):
    class Meta:
        model = PreviousLoan
        fields ='__all__'