from Appcoder import views
from django.urls import path

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar/', views.buscar),
    path('busquedavisitantes',views.busquedaVisitantes, name= 'busquedaVisitantes'),
    path('formulariovisitantes', views.formularioVisitantes, name= 'formularioVisitantes'),
    path('formulariousuarios', views.formularioUsuarios, name= 'formularioUsuarios'),
    path('formulariomoderadores', views.formularioModeradores, name= 'formularioModeradores'),
    path('about/', views.aboutme, name= 'AboutMe'),
]
