from django.urls import path
from.views import GuaranterDelete,GuaranterGet,GuaranterPOst,GuaranterPut

urlpatterns = [
    path('Create/',GuaranterPOst, name='gur_create_url'),
    path('get/',GuaranterGet,name='GUr_get_url'),
    path('upd/<int:id>/',GuaranterPut,name='gur_upd_url'),
    path('delete/<int:id>/', GuaranterDelete, name='guar_delete'),
  

]