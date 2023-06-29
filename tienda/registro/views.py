from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.

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
            return redirect('inicio', {
                'saludo': 'Bienvenido nuevamente'
            })


def signout(request):
    logout(request)
    return render(request, 'registro/logout.html', {
        'despedida': 'Gracias por visitarnos, te esperamos de nuevo pronto'
    })

def soporte(request):
    return render(request, 'registro/soporte.html')

def detalle(request):
    return render(request, 'registro/detalle.html')


