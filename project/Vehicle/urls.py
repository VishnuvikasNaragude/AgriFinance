from django.urls import path
from.views import get,post,put,delete

urlpatterns = [
    path('Create/',post, name='vie_create_url'),
    path('get/',get,name='vie_get_url'),
    path('upd/<int:id>/',put,name='vie_upd_url'),
    path('delete/<int:id>/', delete, name='vie_delete'),
  

]