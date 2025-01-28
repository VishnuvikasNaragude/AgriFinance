from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ServerProfile, ClientProfile

class CustomUserCreationForm(UserCreationForm):
    account_type = forms.ChoiceField(choices=CustomUser.ACCOUNT_TYPE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'account_type')

class ServerProfileForm(forms.ModelForm):
    class Meta:
        model = ServerProfile
        fields = ('server_specific_field',)

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = ('client_specific_field',)


from django import template

register = template.Library()

@register.filter
def add_class(value, class_name):
    return value.as_widget(attrs={'class': class_name})
