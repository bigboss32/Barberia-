from django.shortcuts import render
from apps.terminal.services.crud_estado import Estado
from apps.terminal.services.crud_servicios import Servicios
from apps.terminal.services.crud_ubicacion import Ubicacion
from apps.terminal.services.crud_persona import Persona
from apps.terminal.services.crud_vehiculo import Vehiculo
from apps.terminal.services.crud_venta import Venta

def index(request):
    return render(request, 'index.html')
def crear_estado(request):
    instancia=Estado()
    return instancia.crearestado(request)
def obtener_estado(request):
    instancia=Estado()
    return instancia.obtenerestado(request)
def eliminar_estado(request):
    instancia=Estado()
    return instancia.eliminarestado(request)
def editar_estado(request):
    instancia=Estado()
    return instancia.editarestado(request)
def crear_servicios(request):
    instancia=Servicios()
    return instancia.crearservicio(request)
def obtener_servicios(request):
    instancia=Servicios()
    return instancia.obtenerservicio(request)
def eliminar_servicio(request):
    instancia=Servicios()
    return instancia.eliminarservicio(request)
def editar_servicio(request):
    instancia=Servicios()
    return instancia.editarservicio(request)
def crear_ubicacion(request):
     instancia=Ubicacion()
     return instancia.crearubicacion(request)
def crear_persona(request):
     instancia=Persona()
     return instancia.crearpersona(request)
def crear_documento(request):
     instancia=Persona()
     return instancia.creardocumento(request)
  
def crear_vehiculo(request):
     instancia=Vehiculo()
     return instancia.crearvehiculo(request)

def crear_venta(request):
     instancia=Venta()
     return instancia.crearventa(request)

