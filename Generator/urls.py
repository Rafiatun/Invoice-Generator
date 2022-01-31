from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    
    path('', views.home , name="home"),
    path('addinvoice' , views.AddInvoice , name="addinvoice"),
    path('items',views.Items , name="items"),
    path('updateinvoice/<str:pk>/' , views.Update_Invoice , name='updateinvoice'),
    path('deleteinvoice/<str:pk>/' , views.Delete_Invoice , name="deleteinvoice")
]
