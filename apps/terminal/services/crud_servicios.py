from django.db import connection
from collections import namedtuple
from django.shortcuts import render,redirect

class Servicios():
    def crearservicio(self,request):
        if request.method == 'POST':
             des = request.POST['descripcion']
             estado = request.POST['tipo_estado']
             print(des)
             print(estado)
             with connection.cursor() as cursor:
                 cursor.execute("INSERT INTO data_servicio (servicio, id_estado_id) VALUES (%s, %s)", [des, estado])
                 connection.commit()
                 return redirect('crear_servicios')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM data_estado")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            return render(request, 'servicios/Crear_servicios.html',{'data': data})
    
    def obtenerservicio(self,request):
        if request.method == 'GET':
             with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM data_servicio")
                columnas = [col[0] for col in cursor.description]  # Nombres de columnas
                data = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
                return render(request, 'servicios/obtener_servicios.html', {'data': data})
        return render(request, 'servicios/obtener_servicios.html')
    
    def eliminarservicio(self,request):
        if request.method == 'POST':
            servicio_id=request.POST['id']
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM data_servicio WHERE id = %s", [servicio_id])
                return redirect('obtener_servicios')
        return render(request, 'servicios/obtener_servicios.html') 

    def editarservicio(self,request):
          if request.method == 'POST':
            servico_id=request.POST['id']
            des=request.POST['descripcion']
            with connection.cursor() as cursor:
                cursor.execute("UPDATE data_servicio SET servicio = %s WHERE id = %s", [des, servico_id])
                return redirect('obtener_servicios')
          return render(request, 'servicios/obtener_servicios.html') 