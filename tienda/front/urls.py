from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='quienessomos'),
]
