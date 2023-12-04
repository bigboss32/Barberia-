from django.urls import path
from .views import iniciar_sesion,registrar_usuario,cerrar_sesion

urlpatterns = [
    path("",iniciar_sesion, name='iniciar_sesion'),
    path("registrar/", registrar_usuario, name='registrar_usuario'),
    path("cerrar_sesion/", cerrar_sesion, name='cerrar_sesion'),
]
