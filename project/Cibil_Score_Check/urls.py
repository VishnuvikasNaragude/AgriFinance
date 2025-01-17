from django.urls import path
from .views import CibilView,CibilGet,cibilPut,cibilDelete

urlpatterns =[
    path('cibilpost/',CibilView,name='cibil_post_urls'),
    path('cibilget/',CibilGet,name="cibil_get"),
    path('cibilput/<int:id>/',cibilPut,name='CIbil_put_url'),
    path('cibildel/<int:id>/',cibilDelete,name='CIbil_del_url')
]