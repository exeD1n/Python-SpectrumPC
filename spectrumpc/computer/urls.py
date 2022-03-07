from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('computer', views.computer, name='computer'),
    path('periphery', views.periphery, name='periphery'),
]