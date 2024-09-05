from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm

# Create your views here.

def login_request(request):

    msg_login = "Bienvenido!"
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "Appcoder/inicio.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "USERS/login.html", {"form": form, "msg_login": msg_login})


def register(request):

    msg_register = "Registrado exitosamente."
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"Appcoder/inicio.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"USERS/registro.html" ,  {"form":form, "msg_register": msg_register})



def cerrar_sesion(req):
    if req.method == 'GET':
        logout(req)
        return render(req, 'USERS/logout.html')
    return render(req, 'Appcoder/inicio.html')


