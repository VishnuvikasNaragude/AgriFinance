"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')), 
    path('Enqe/',include('Enquiry.urls')),
    path('Cust/',include('Customer.urls')),
    path('cibil/',include('Cibil_Score_Check.urls')),
    path('add/',include('addressId.urls')),
    path('guar/',include('Guaranter.urls')),
    path('pre/',include('PreviousLoan.urls')),
    path('bank/',include('BankDetails.urls')),
    path('doc/',include('DocumentDetails.urls')),
    path('vehicle/',include('Vehicle.urls')),
    path('accounts/',include('account.urls')),


    
]
