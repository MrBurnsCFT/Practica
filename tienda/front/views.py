from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'front/index.html')

def productos(request):
    return render(request, 'front/productos.html')

def contacto(request):
    return render(request, 'front/contacto.html')
