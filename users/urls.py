from django.urls import path 
from users import views
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns =[
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', views.cerrar_sesion, name='Logout'),
    path('edit/', views.editar_perfil, name="EditarPerfil"),
    path('cambiarContrasenia/', views.CambiarContrasenia.as_view(), name='cambiarContrasenia'),

]