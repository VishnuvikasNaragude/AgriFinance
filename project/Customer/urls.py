from django.urls import path
from .views import CustomerView,CustomerDetails,CustomerUpdate,CustomerDelete

urlpatterns= [
    path('post/',CustomerView,name='C_post_url'),
    path('get/',CustomerDetails,name='C_get_url'),
    path('upd/<int:id>/',CustomerUpdate,name='C_put_url'),
     path('delete/<int:id>/',CustomerDelete,name='C_del_url')

]
