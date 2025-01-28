from django.shortcuts import render
from .models import ServerProfile, ClientProfile
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .form import CustomUserCreationForm, ServerProfileForm, ClientProfileForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            account_type = form.cleaned_data['account_type']
            
            # Create a profile based on account type
            if account_type == 'server':
                ServerProfile.objects.create(user=user, server_specific_field='Default Server Info')
            elif account_type == 'client':
                ClientProfile.objects.create(user=user, client_specific_field='Default Client Info')
            
            # Log the user in and redirect
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def server_register(request):
    # Your logic here
    return render(request, 'server_register.html')

def client_register(request):
    # Your logic here
    return render(request, 'client_register.html')


def home(request):
    return render(request, 'home.html')
