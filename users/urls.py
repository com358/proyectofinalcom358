from django.urls import path 
from users import views
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns =[
    path('accounts/login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', views.cerrar_sesion, name='Logout')


]