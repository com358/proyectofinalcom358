from Appcoder import views
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('formularioUsuarios', views.FormularioUsuarios, name= 'formularioUsuarios'),
    path('rojo', views.rojo, name='rojo'),
    path('azul', views.azul, name='azul'),
    path('verde', views.verde, name='verde'),
    path('amarillo', views.amarillo, name= 'amarillo'),
]
