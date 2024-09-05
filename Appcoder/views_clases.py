from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Appcoder.forms import FormularioVisitantes, FormularioUsuarios, FormularioModeradores

# Create your views here.
class VisitantesCreateView(LoginRequiredMixin,CreateView):
    model = Visitantes
    form_class = FormularioVisitantes
    template_name = 'visitantes_form.html'
    success_url = reverse_lazy('visitantes-list')
