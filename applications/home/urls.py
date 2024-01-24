from django.urls import path

from .views import *

app_name = 'home_app'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    #path('inicio/', inicio, name='inicio'),
    path('inicio/', Inicio.as_view(), name='inicio'),
]