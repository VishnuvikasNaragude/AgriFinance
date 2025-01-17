from django.urls import path
from .views import BankDetailsDelete,BankDetailsget,BankDetailspostView,BankDetailsUpdate


urlpatterns = [
    path('Create/',BankDetailspostView, name='bank_create_url'),
    path('get/',BankDetailsget,name='bank_get_url'),
    path('upd/<int:id>/',BankDetailsUpdate,name='bank_upd_url'),
    path('delete/<int:id>/', BankDetailsDelete, name='bank_delete'),
  

]