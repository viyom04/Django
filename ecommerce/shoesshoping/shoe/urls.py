from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path('shopingpage', views.shopingpage, name= "shopingpage")
]