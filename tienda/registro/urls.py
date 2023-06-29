from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='registrarse'),
    path('signin/', views.signin, name='ingresar'),
    path('logout/', views.signout, name='logout'),
    path('soporte/', views.soporte, name='soporte'),
    path('soporte/detalle/', views.detalle, name='detalle'),
]
