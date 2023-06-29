from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='registrarse'),
    path('signin/', views.signin, name='ingresar'),
    path('logout/', views.signout, name='logout'),
    path('reporte/', views.reporte, name='soporte'),
    path('soporte/listado/', views.listado, name='listado'),
    path('soporte/<int:reporte_id>/', views.detalle, name='detalle'),
]
