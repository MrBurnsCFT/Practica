from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ReporteForm
from .models import Reporte
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def base(request):
    return render(request, 'registro/base.html')

def home(request):
    return render(request, 'registro/home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'registro/signup.html', {
            'form': UserCreationForm
        })
    else :
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return render(request, 'front/index.html', {
                    'mensaje': 'User created successfully'
                })
            except IntegrityError:
                return render(request, 'registro/signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request, 'registro/signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

def signin(request):
    if request.method == 'GET':
        return render(request, 'registro/signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], 
        password=request.POST['password'])
        if user is None:
            return render(request, 'registro/signin.html',{
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return render(request, 'front/index.html', {
                'saludo': 'Bienvenido nuevamente'
            })

@login_required
def signout(request):
    logout(request)
    return render(request, 'registro/logout.html', {
        'despedida': 'Gracias por visitarnos, te esperamos de nuevo pronto'
    })

@login_required
def reporte(request):
    if request.method == 'GET':
        return render(request, 'registro/reporte.html', {
            'form': ReporteForm
        })
    else:
        try:
            form = ReporteForm(request.POST)
            new_reporte = form.save(commit=False)
            new_reporte.user = request.user
            new_reporte.save()
            return render(request, 'registro/reporte.html')
        except ValueError:
            return render(request, 'registro/reporte.html', {
                'form': ReporteForm,
                'error': 'Complete todos los campos'
            })
            
@login_required            
def listado(request):
    reportes = Reporte.objects.filter(user=request.user)
    return render(request, 'registro/listado.html', {'reportes': reportes})

@login_required
def detalle(request, reporte_id):
    reporte = get_object_or_404(Reporte, pk=reporte_id)
    return render(request, 'registro/detalle.html')


