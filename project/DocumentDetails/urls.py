from django.urls import path
from.views import DocumentDetailsPOst,DocumentDetailsGet,DocumentDetailsPut,DocumentDetailsDelete

urlpatterns = [
    path('Create/',DocumentDetailsPOst, name='doc_create_url'),
    path('get/',DocumentDetailsGet,name='doc_get_url'),
    path('upd/<int:id>/',DocumentDetailsPut,name='doc_upd_url'),
    path('delete/<int:id>/', DocumentDetailsDelete, name='doc_delete'),
  

]