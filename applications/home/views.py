from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



#
class Home( TemplateView):
    template_name = "home/home.html"
    #login_url = reverse_lazy('users_app:login')

#
class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'home/bienvenida.html'
    context_object_name = 'items'
    paginate_by = 10
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context