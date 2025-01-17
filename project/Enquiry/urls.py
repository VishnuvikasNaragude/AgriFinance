from django.urls import path
from .views import EnqueryView,EnqueryShow,EnqueryUpdate,EnqueryDelete

urlpatterns = [
    path('Create/',EnqueryView, name='create_url'),
    path('get/',EnqueryShow,name='get_url'),
    path('upd/<int:id>/',EnqueryUpdate,name='upd_url'),
    path('delete/<int:id>/', EnqueryDelete, name='enquiry_delete'),
  

]