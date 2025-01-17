from django.urls import path
from .views import PreviousLoanDelete,PreviousLoanPOst,PreviousLoanGet,PreviousLoanPut


urlpatterns = [
    path('Create/',PreviousLoanPOst, name='pre_create_url'),
    path('get/',PreviousLoanGet,name='pre_get_url'),
    path('upd/<int:id>/',PreviousLoanPut,name='pre_upd_url'),
    path('delete/<int:id>/', PreviousLoanDelete, name='pre_delete'),
  

]