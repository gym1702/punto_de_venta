from django.shortcuts import render, redirect
from django.views.generic import View, ListView, UpdateView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.messages.views import SuccessMessageMixin
from datetime import date
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django .contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


from .forms import UserRegisterForm, LoginForm, CambiarPassForm, VerificacionForm
from .models import User

from applications.empresa.models import Empresa

# from applications.citas.models import Cita
# from applications.expedientes.models import Consulta, HGenral, HOrto, Notas

# #from applications.cita.models import Cita
# #from applications.expedientes.models import HGenral, HOrto, Consulta, Notas
# from applications.pacientes.models import Paciente
# from applications.pacientes.forms import PacienteForm
# from applications.medicos.models import Medico 
# from applications.presupuestos.models import Presupuesto, Pago, PagoHistorial  
# from applications.recetas.models import Receta  

from .functions import generador_codigo
#from applications.pacientes.functions import generador_num_registro



#verifica que nombre no se repita
@login_required(login_url='beses:login')
@permission_required('usuario.change_usuario', login_url='bases:login')
def verificar_usuario_existe(request):
    usuario = request.GET.get('full_name')

    #Realiza la consulta en la base de datos para verificar si el cliente ya existe.
    existe = User.object.filter(full_name=usuario).exists()   

    data = {'existe': existe}
    return JsonResponse(data)



#
class UsuariosListar(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = User
    permission_required = "usuario.view_usuario"
    template_name = 'users/listar.html'
    context_object_name = 'obj'

    #uTILIZADO PARA LOGO Y FAVICON
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['empresa'] = Empresa.objects.get()

        return context


#
class UsuarioEditar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'usuario.change_usuario'
    model = User
    template_name = 'users/register.html'
    context_object_name = 'obj'
    form_class = UserRegisterForm
    success_url = reverse_lazy("users_app:usuarios_listar")
    success_message = ("Usuario actualizado correctamente")   


#     def form_valid(self, form):
#         if form.is_valid():
#             form.instance.usuario_edita = self.request.user.full_name
#             form.save()
#         else:
#             pass    
        

#         return super().form_valid(form)



###
class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '.'
    #login_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        #generar codigo de registro
        codigo = generador_codigo()

        #crea usuario
        User.object.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['pass1'],
            full_name = form.cleaned_data['full_name'],
            tipo = form.cleaned_data['tipo'],
            telefono = form.cleaned_data['telefono'],
            cod_registro = codigo
        )


        #recuperer permisos que tendra paciente 
        # usuario = User.object.filter().last()
        # content_type_cita = ContentType.objects.get_for_model(Cita)
        # cita_permission = Permission.objects.filter(content_type = content_type_cita)
        # print([perm_cita.codename for perm_cita in cita_permission])
        # #asignar permiso  
        # for perm_cita in cita_permission:  
        #     if usuario.tipo == 'Paciente':
        #         usuario.user_permissions.add(perm_cita)
        #     else:
        #         pass
           

        #enviar codigo a email de usuario
        # asunto = 'Confirmacion de email'
        # mensaje = 'El código de verificación para activar su cuenta es: ' + codigo
        # email_remitente = 'rgrsistemas@gmail.com'
        # send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        
        #redirigir a pantalla de validacion
        # return HttpResponseRedirect(reverse('users_app:usuario_verificacion', kwargs={'pk': usuario.id}))
        return HttpResponseRedirect(reverse('users_app:usuarios_listar'))
    

    #contexto para cargar imagenes y logos de footer y navbar
    def get_context_data(self, **kwargs):
        context = super(UserRegisterView, self).get_context_data(**kwargs)

        #context["home"] = Home.objects.en_home()
        return context


###
class Login(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:inicio')

    def form_valid(self, form):
        user = authenticate(
            email= form.cleaned_data['email'],
            password= form.cleaned_data['password']
        )
        login(self.request, user)

        return super(Login, self).form_valid(form)

    #contexto para cargar imagenes y logos de footer y navbar
    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)

        #context["home"] = Home.objects.en_home()
        return context


###
class Logout(View):

    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(reverse('users_app:login'))


###
class CambiarPassword(LoginRequiredMixin, FormView):
    template_name = 'users/cambiar_pass.html'
    form_class = CambiarPassForm
    success_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            email= usuario.email,
            password= form.cleaned_data['password1']
        )

        if user:
            new_pass = form.cleaned_data['password2']
            usuario.set_password(new_pass)
            usuario.save()

        logout(self.request)
        return super(CambiarPassword, self).form_valid(form)
    
    
    #contexto para cargar imagenes y logos de footer y navbar
    def get_context_data(self, **kwargs):
        context = super(CambiarPassword, self).get_context_data(**kwargs)

        #context["home"] = Home.objects.en_home()
        return context


###
class CodVerificacionView(FormView):
    template_name = 'users/verificacion.html'
    form_class = VerificacionForm
    success_url = reverse_lazy('users_app:login')

    def get_form_kwargs(self):
        kwargs = super(CodVerificacionView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):
        User.object.filter(id=self.kwargs['pk']).update(is_active=True)

        return super(CodVerificacionView, self).form_valid(form)



###
# class PacienteRegisterCrear(SuccessMessageMixin, MixinFormInvalid, CreateView):
#     model = Paciente
#     permission_required = 'pacientes.add_paciente'
#     template_name = 'users/registrar_nuevo.html'
#     context_object_name = 'obj'
#     form_class = PacienteForm
#     success_url = reverse_lazy("users_app:login")
#     login_url = 'bases:login'
#     success_message = ("y su contraseña es: 123456, \
#                        una vez dentro de su perfil, podra cambiar su clave de acceso dando click en su nombre.")

#     #Crea paciente
#     def form_valid(self, form):
#         num_reg = generador_num_registro()

#         #form.instance.usuario_crea = self.request.user
#         form.instance.num_registro = num_reg
#         form.instance.edad = (date.today().year - form.instance.fecha_nac.year)
#         form.instance.medico = form.instance.medico
        
#         form.save()

#         #Asigna no. expediente
#         form.instance.no_expediente = form.instance.pk
#         form.save()        


#         #Crear Usuario de acceso al sistema
#         pac = Paciente.objects.latest('id')
        
#         usuario = User(
#             email = pac.email,
#             password = make_password('123456'),
#             full_name = pac.full_name,
#             telefono = pac.telefono,
#             tipo = 'Paciente',
#             num_registro = num_reg,
#             is_active = True,                       
#         )
#         usuario.save()

#         #Mensaje complementario  para inicio de sesion
#         messages.success(self.request, "Registro creado exitosamente, su email es: " + pac.email)


#         #Crear Historia clinica general
#         hcg = HGenral.objects.filter(no_expediente=form.instance.pk).first()
#         if not hcg: 
#             hist = HGenral(
#                 paciente = Paciente.objects.latest('id'),
#                 no_historia = form.instance.pk,
#                 no_expediente = form.instance.pk,
#                 medico = form.instance.medico,
#             )
#             hist.save()


#         #Crear Historia clinica de ortodoncia
#         hco = HOrto.objects.filter(no_expediente=form.instance.pk).first()
#         if not hco: 
#             hist = HOrto(
#                 paciente = Paciente.objects.latest('id'),
#                 hgral = HGenral.objects.latest('id'),
#                 no_historia = form.instance.pk,
#                 no_expediente = form.instance.pk,
#                 medico = form.instance.medico,
#             )
#             hist.save()


#         #Crear Expediente Consulta
#         cons = Consulta.objects.filter(no_expediente=form.instance.pk).first()
#         if not cons: 
#             consul = Consulta(
#                 paciente = Paciente.objects.latest('id'),
#                 hgral = HGenral.objects.latest('id'),
#                 horto = HOrto.objects.latest('id'),
#                 no_expediente = form.instance.pk,
#                 medico = form.instance.medico,
#             )
#             consul.save()

        
        
#         #recuperer permisos que tendra paciente 
#         content_type_cita = ContentType.objects.get_for_model(Cita)
#         cita_permission = Permission.objects.filter(content_type = content_type_cita)
#         print([perm_cita.codename for perm_cita in cita_permission])
#         #asignar permiso  
#         for perm_cita in cita_permission:      
#             if usuario.tipo == 'Paciente':
#                 usuario.user_permissions.add(perm_cita)
#             else:
#                 pass


#         content_type_presupuesto = ContentType.objects.get_for_model(Presupuesto)
#         presupuesto_permission = Permission.objects.filter(content_type = content_type_presupuesto)
#         print([perm_presupuesto.codename for perm_presupuesto in presupuesto_permission])
#         #asignar permiso  
#         for perm_presupuesto in presupuesto_permission:      
#             if usuario.tipo == 'Paciente':
#                 usuario.user_permissions.add(perm_presupuesto)
#             else:
#                 pass

        
#         content_type_receta = ContentType.objects.get_for_model(Receta)
#         receta_permission = Permission.objects.filter(content_type = content_type_receta)
#         print([perm_receta.codename for perm_receta in receta_permission])
#         #asignar permiso  
#         for perm_receta in receta_permission:      
#             if usuario.tipo == 'Paciente':
#                 usuario.user_permissions.add(perm_receta)
#             else:
#                 pass
        

#         content_type_pago = ContentType.objects.get_for_model(Pago)
#         pago_permission = Permission.objects.filter(content_type = content_type_pago)
#         print([perm_pago.codename for perm_pago in pago_permission])
#         #asignar permiso  
#         for perm_pago in pago_permission:      
#             if usuario.tipo == 'Paciente':
#                 usuario.user_permissions.add(perm_pago)
#             else:
#                 pass

        
#         content_type_pagoHistorial = ContentType.objects.get_for_model(PagoHistorial)
#         pagoHistorial_permission = Permission.objects.filter(content_type = content_type_pagoHistorial)
#         print([perm_pagoHistorial.codename for perm_pagoHistorial in pagoHistorial_permission])
#         #asignar permiso  
#         for perm_pagoHistorial in pagoHistorial_permission:      
#             if usuario.tipo == 'Paciente':
#                 usuario.user_permissions.add(perm_pagoHistorial)
#             else:
#                 pass
 

#         return super().form_valid(form)
    
    

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         medicos = Medico.objects.all()               
#         context['medicos_all'] = medicos 
        
#         return context
    


