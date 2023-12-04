from django.shortcuts import render
from apps.terminal.services.crud_estado import Estado
from apps.terminal.services.crud_servicios import Servicios
from apps.terminal.services.crud_ubicacion import Ubicacion
from apps.terminal.services.crud_persona import Persona
from apps.terminal.services.crud_vehiculo import Vehiculo
from apps.terminal.services.crud_venta import Venta
from apps.terminal.services.crud_horario import Horario

from django.db import connection
from django.shortcuts import render
def index(request):
    with connection.cursor() as cursor:
     cursor.execute("SELECT COUNT(*) FROM data_venta")
     columnas = [col[0] for col in cursor.description]  
     catidad_ventas = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
     cursor.execute("SELECT COUNT(*) FROM data_vehiculo")
     columnas = [col[0] for col in cursor.description] 
     catidad_vehiculo = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
     cursor.execute("SELECT COUNT(*) FROM data_conductor")
     columnas = [col[0] for col in cursor.description] 
     catidad_conductor = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
     cursor.execute("SELECT COUNT(*) FROM data_usuario")
     columnas = [col[0] for col in cursor.description] 
     data_usuario = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
     cursor.execute("SELECT COUNT(*) FROM data_terminal")
     columnas = [col[0] for col in cursor.description] 
     data_terminal = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
     cursor.execute("SELECT COUNT(*) FROM data_ruta")
     columnas = [col[0] for col in cursor.description] 
     data_ruta = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
     cursor.execute("SELECT COUNT(*) FROM data_servicio")
     columnas = [col[0] for col in cursor.description] 
     data_servicio = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
     cursor.execute("SELECT COUNT(*) FROM data_ciudad")
     columnas = [col[0] for col in cursor.description] 
     data_ciudad = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

     cursor.execute("""
        SELECT data_venta.*, data_estado.*
        FROM data_venta
        JOIN data_estado ON data_venta.id_estado_id = data_estado.id
    """)
     columnas = [col[0] for col in cursor.description]
     filas = cursor.fetchall()
     resultado = [dict(zip(columnas, fila)) for fila in filas]

     cursor.execute("""
        SELECT SUM(totalbruto) AS total_ventas
        FROM data_venta
    """)
     columnas = [col[0] for col in cursor.description]
     filas = cursor.fetchall()
     totalbruto = [dict(zip(columnas, fila)) for fila in filas]
 
 
     return render(request, 'index.html',{"catidad_ventas":catidad_ventas[0]['count'],
                                          "cantidad_veh":catidad_vehiculo[0]['count'],
                                           "catidad_conductor":catidad_conductor[0]['count'],
                                           "data_usuario":data_usuario[0]['count'],
                                           "data_terminal":data_terminal[0]['count'],
                                           "data_ruta":data_ruta[0]['count'],
                                           "data_ciudad":data_ciudad[0]['count'],
                                           "data_servicio":data_servicio[0]['count'],
                                           "data_venta_con":resultado,
                                           "totalbruto":totalbruto[0]['total_ventas'],

                                          })

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

def listar_venta(request):
     instancia=Venta()
     return instancia.listarventa(request)

def crear_horario(request):
    instancia=Horario()
    return instancia.crearhorario(request)
    

