from django.urls import path

from . import views


app_name = 'users_app'

urlpatterns = [
    path('usuario-listar/', views.UsuariosListar.as_view(), name='usuarios_listar'),
    path('usuario-crear/', views.UserRegisterView.as_view(), name='usuarios_crear'),
    path('usuario-editar/<int:pk>/', views.UsuarioEditar.as_view(), name='usuarios_editar'),

    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('cambiar-pass', views.CambiarPassword.as_view(), name='cambiar_pass'),
    path('usuario-verificacion/<pk>/', views.CodVerificacionView.as_view(), name='usuario_verificacion'),
    #path('nuevo-paciente/', views.PacienteRegisterCrear.as_view(), name='crear_nuevo_paciente'),

    path('verificar_usuario_existe/', views.verificar_usuario_existe, name='verificar_usuario_existe'),
]