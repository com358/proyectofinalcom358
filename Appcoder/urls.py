from Appcoder import views
from django.urls import path

urlpatterns = [
    path('busquedavisitantes', views.inicio, name='inicio'),
    path('buscar/', views.buscar),
    path('',views.busquedaVisitantes, name= 'busquedaVisitantes'),
    path('formulariovisitantes', views.formularioVisitantes, name= 'formularioVisitantes'),
    path('formulariousuarios', views.formularioUsuarios, name= 'formularioUsuarios'),
    path('formulariomoderadores', views.formularioModeradores, name= 'formularioModeradores'),
    path('rojo', views.rojo, name='rojo'),
    path('azul', views.azul, name='azul'),
    path('verde', views.verde, name='verde'),
    path('amarillo', views.amarillo, name= 'amarillo'),
]
