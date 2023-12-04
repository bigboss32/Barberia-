from django.db import connection
from collections import namedtuple
from django.shortcuts import render,redirect
class Ubicacion():
    def crearubicacion(self,request):
        if request.method == 'POST':
             nombre = request.POST['nombre']
             estado = request.POST['tipo_estado']
             ciudad = request.POST['ciudad']
             tipo_estado_ciudad = request.POST['tipo_estado_ciudad']
         
             with connection.cursor() as cursor:
                 cursor.execute("INSERT INTO data_departamento (nombre, id_estado_id) VALUES (%s, %s)", [nombre, estado])
                 cursor.execute("SELECT LASTVAL()")
                 id = cursor.fetchone()[0]
                 cursor.execute("INSERT INTO data_ciudad (nombre, id_departamento_id,id_estado_id) VALUES (%s, %s,%s)", [ciudad,id,tipo_estado_ciudad])
                 connection.commit()
                 return redirect('crear_ubicacion')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM data_estado")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            return render(request, 'ubicacion/Crear_ubicacion.html',{'data': data})