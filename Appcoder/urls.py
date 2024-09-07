from Appcoder import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.aboutme, name= 'AboutMe'),

     ##### VISITANTES ###################################
    path('visitantes-list/', views.VisitantesListView.as_view(), name="VisitantesList"),
    path('visitantes-detail/<int:pk>/', views.VisitantesDetailView.as_view(), name="VisitantesDetail"), 
    path('visitantes-create/', views.VisitantesCreateView.as_view(), name="VisitantesCreate"),
    path('visitantes-update/<int:pk>/', views.VisitantesUpdateView.as_view(), name="VisitantesUpdate"),
    path('visitantes-delete/<int:pk>/', views.VisitantesDeleteView.as_view(), name="VisitantesDelete"),
    #####################################################

    ##### USUARIOS ###################################
    path('usuarios-list/', views.UsuariosListView.as_view(), name="UsuariosList"),
    path('usuarios-detail/<int:pk>/', views.UsuariosDetailView.as_view(), name="UsuariosDetail"), 
    path('usuarios-create/', views.UsuariosCreateView.as_view(), name="UsuariosCreate"),
    path('usuarios-update/<int:pk>/', views.UsuariosUpdateView.as_view(), name="UsuariosUpdate"),
    path('usuarios-delete/<int:pk>/', views.UsuariosDeleteView.as_view(), name="UsuariosDelete"),
    #####################################################

     ##### MODERADORES ###################################
    path('moderadores-list/', views.ModeradoresListView.as_view(), name="ModeradoresList"),
    path('moderadores-detail/<int:pk>/', views.ModeradoresDetailView.as_view(), name="ModeradoresDetail"), 
    path('moderadores-create/', views.ModeradoresCreateView.as_view(), name="ModeradoresCreate"),
    path('moderadores-update/<int:pk>/', views.ModeradoresUpdateView.as_view(), name="ModeradoresUpdate"),
    path('moderadores-delete/<int:pk>/', views.ModeradoresDeleteView.as_view(), name="ModeradoresDelete"),
    #####################################################
]


