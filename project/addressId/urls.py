from django.urls import path
from .views import AddresPOST,AddresGet,AddresPut,AddresDelete


urlpatterns =[
    path('post/',AddresPOST,name='add_poat'),
    path('get/',AddresGet,name='ADD_get'),
    path('put/<int:id>',AddresPut,name='ADD_put'),
    path('del/<int:id>',AddresDelete,name='ADD_del'),
]