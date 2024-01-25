"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
#
from django.conf.urls import handler404
#from applications.home.views import Error404View


urlpatterns = [
    path('admin/', admin.site.urls),

    re_path('', include('applications.home.urls')),
    re_path('', include('applications.users.urls')),   
    re_path('', include('applications.empresa.urls')), 
    re_path('', include('applications.clientes.urls')),
    re_path('', include('applications.categorias.urls')),
    re_path('', include('applications.marcas.urls')),
    re_path('', include('applications.proveedores.urls')),
    re_path('', include('applications.productos.urls')),

    
    # re_path('', include('applications.medicos.urls')),
    
    # re_path('', include('applications.expedientes.urls')),    
    # re_path('', include('applications.citas.urls')),
    # re_path('', include('applications.asistentes.urls')),
    # re_path('', include('applications.secretarias.urls')),
    # re_path('', include('applications.servicios.urls')),
    # re_path('', include('applications.medicamentos.urls')),
    # re_path('', include('applications.presupuestos.urls')),
    # re_path('', include('applications.recetas.urls')),    
    # re_path('', include('applications.consentimiento.urls')),
    # re_path('', include('applications.mantto.urls')),


    
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#MANEJO DE ERROR 404
#handler404 = Error404View.as_view()
