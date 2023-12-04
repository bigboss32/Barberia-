from django.urls import path
from .views import *

urlpatterns = [
   
    path("terminal/",index, name='index'),
    path("terminal/crear_estado/",crear_estado, name='crear_estado'),
    path("terminal/obtener_estado/",obtener_estado, name='obtener_estado'),
    path("terminal/eliminar_estado/",eliminar_estado, name='eliminar_estado'),
    path("terminal/editar_estado/",editar_estado, name='editar_estado'),
    path("terminal/crear_servicios/",crear_servicios, name='crear_servicios'),
    path("terminal/obtener_servicios/",obtener_servicios, name='obtener_servicios'),
    path("terminal/eliminar_servicio/",eliminar_servicio, name='eliminar_servicio'),
    path("terminal/editar_servicio/",editar_servicio, name='editar_servicio'),
    path("terminal/crear_ubicacion/",crear_ubicacion, name='crear_ubicacion'),
    path("terminal/crear_persona/",crear_persona, name='crear_persona'),
    path("terminal/crear_documento/",crear_documento, name='crear_documento'),
    path("terminal/crear_vehiculo/",crear_vehiculo, name='crear_vehiculo'),
    path("terminal/crear_venta/",crear_venta, name='crear_venta'),
    path("terminal/listar_venta/",listar_venta, name='listar_venta'),
    path("terminal/crear_horario/",crear_horario, name='crear_horario'),
    
]