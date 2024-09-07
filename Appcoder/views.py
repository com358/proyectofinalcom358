from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import Visitantes, Usuarios, Moderadores
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


#VISITANTES #################################
class VisitantesListView(LoginRequiredMixin, ListView):
    model = Visitantes
    template_name = "appcoder/visitantes_list.html"

class VisitantesCreateView(LoginRequiredMixin,CreateView):
    model = Visitantes
    template_name = 'appcoder/visitantes_create.html'
    fields = ["nombre", "color_favorito"]
    success_url=reverse_lazy("VisitantesList")

class VisitantesDetailView(LoginRequiredMixin,DetailView):
      model = Visitantes
      template_name = "appcoder/visitantes_detail.html"

class VisitantesUpdateView(LoginRequiredMixin, UpdateView):
    model = Visitantes
    success_url = reverse_lazy("VisitantesList")
    fields = ["nombre", "color_favorito"]
    template_name = "appcoder/visitantes_update.html"

class VisitantesDeleteView(LoginRequiredMixin, DeleteView):
    model = Visitantes
    success_url = reverse_lazy("VisitantesList")
    template_name = 'appcoder/visitantes_confirm_delete.html'

#############################################

#USUARIOS #################################
class UsuariosListView(LoginRequiredMixin, ListView):
    model = Usuarios
    template_name = "appcoder/usuarios_list.html"

class UsuariosCreateView(LoginRequiredMixin,CreateView):
    model = Usuarios
    template_name = 'appcoder/usuarios_create.html'
    fields = ["nombre","mail","color_favorito"]
    success_url=reverse_lazy("UsuariosList")

class UsuariosDetailView(LoginRequiredMixin,DetailView):
      model = Usuarios
      template_name = "appcoder/usuarios_detail.html"

class UsuariosUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuarios
    success_url = reverse_lazy("UsuariosList")
    fields = ["nombre","mail","color_favorito"]
    template_name = "appcoder/usuarios_update.html"

class UsuariosDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuarios
    success_url = reverse_lazy("UsuariosList")
    template_name = 'appcoder/usuarios_confirm_delete.html'

#############################################

#MODERADORES #################################
class ModeradoresListView(LoginRequiredMixin, ListView):
    model = Moderadores
    template_name = "appcoder/moderadores_list.html"

class ModeradoresCreateView(LoginRequiredMixin,CreateView):
    model = Moderadores
    template_name = 'appcoder/moderadores_create.html'
    fields = ['nombre', 'mail', 'password'] 
    success_url=reverse_lazy("ModeradoresList")

class ModeradoresDetailView(LoginRequiredMixin,DetailView):
      model = Moderadores
      template_name = "appcoder/moderadores_detail.html"

class ModeradoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Moderadores
    success_url = reverse_lazy("ModeradoresList")
    fields = ['nombre', 'mail', 'password'] 
    template_name = "appcoder/moderadores_update.html"

class ModeradoresDeleteView(LoginRequiredMixin, DeleteView):
    model = Moderadores
    success_url = reverse_lazy("ModeradoresList")
    template_name = 'appcoder/moderadores_confirm_delete.html'

#############################################

def inicio(req):
    return render(req, "appcoder/inicio.html")

def aboutme(req):
      return render(req, "appcoder/about.html")