from django.urls import path
from .views import index,crear_cita

urlpatterns = [
   
    path("sesion/",index, name='index'),
    path("sesion/crear_cita/",crear_cita, name='crear_cita'),

]
