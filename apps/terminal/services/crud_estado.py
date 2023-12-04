from django.db import connection
from collections import namedtuple
from django.shortcuts import render,redirect
class Estado():
    def crearestado(self,request):
        if request.method == 'POST':
             des = request.POST['descripcion']
             with connection.cursor() as cursor:
                 cursor.execute("INSERT INTO data_estado (descripcion_estado) VALUES (%s)", [des])
                 connection.commit()
        return render(request, 'estado/Crear_estado.html')
    
    def obtenerestado(self,request):
        if request.method == 'GET':
             with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM data_estado")
                columnas = [col[0] for col in cursor.description]  # Nombres de columnas
                data = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
                return render(request, 'estado/obtener_estado.html', {'data': data})
        return render(request, 'estado/obtener_estado.html')
    
    def eliminarestado(self,request):
        if request.method == 'POST':
            estado_id=request.POST['id']
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM data_estado WHERE id = %s", [estado_id])
                return redirect('obtener_estado')
        return render(request, 'estado/obtener_estado.html') 

    def editarestado(self,request):
          if request.method == 'POST':
            estado_id=request.POST['id']
            des=request.POST['descripcion']
            with connection.cursor() as cursor:
                cursor.execute("UPDATE data_estado SET descripcion_estado = %s WHERE id = %s", [des, estado_id])
                return redirect('obtener_estado')
          return render(request, 'estado/obtener_estado.html') 
    
