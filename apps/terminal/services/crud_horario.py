from django.db import connection
from collections import namedtuple
from django.shortcuts import render,redirect
class Horario():
    def crearhorario(self, request):
        if request.method == 'POST':
            Ruta = request.POST.get('Ruta', '')
            estado = request.POST.get('estado', '')
            Vehiculo = request.POST.get('Vehiculo', '')
            fecha_venta = request.POST.get('fecha_venta', '')
            totalneto = request.POST.get('totalneto', '')
            totalbruto = request.POST.get('totalbruto', '')
            procentajedescuento = request.POST.get('procentajedescuento', '')
            Estado_Cliente = request.POST.get('Estado_Cliente', '')
            data_persona = request.POST.get('data_persona', '')
            fecha_registro = request.POST.get('fecha_registro', '')
            tiqvehiculo = request.POST.get('tiqvehiculo', '')
            puesto = request.POST.get('puesto', '')
            name=str(request.user)
            iva = request.POST.get('iva', '')
            ivas=int(iva)/100
            totalbrutoconiva=(ivas*float(totalbruto))
            totalconiva=totalbrutoconiva+float(totalbruto)
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO data_venta (totalneto,totalbruto,procentajedescuento,ventafecha,id_estado_id,id_ruta_id,id_vehiculo_id) VALUES (%s, %s,%s, %s,%s, %s,%s)", 
                                [totalneto, totalbruto,procentajedescuento,fecha_venta,estado,Ruta,Vehiculo])
                cursor.execute("SELECT LASTVAL()")
                id_venta= cursor.fetchone()[0]
                cursor.execute("INSERT INTO data_cliente (fecha_registro,id_persona_id,id_estado_id) VALUES (%s, %s,%s)", 
                                [fecha_registro, data_persona,Estado_Cliente])
                cursor.execute("SELECT LASTVAL()")
                id_cliente= cursor.fetchone()[0]
                cursor.execute("INSERT INTO data_usuario(id_persona_id,id_estado_id,name) VALUES (%s, %s,%s)", 
                                [data_persona, estado,name])
                cursor.execute("SELECT LASTVAL()")
                id_user= cursor.fetchone()[0]
                cursor.execute("INSERT INTO data_tiquete(id_cliente_id,id_usuario_id,id_estado_id,id_venta_id,tiqvehiculo,puesto,totalbruto,iva,totalmasiva,descuento) VALUES (%s, %s,%s,%s,%s,%s, %s,%s,%s,%s)", 
                                [id_cliente, id_user,Estado_Cliente,id_venta,tiqvehiculo,puesto,totalbruto,iva,totalconiva,procentajedescuento,])
                return redirect('crear_venta')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM data_estado")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            cursor.execute("SELECT * FROM data_ruta")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data_ruta = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            cursor.execute("SELECT * FROM data_vehiculo")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data_vehiculo = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            cursor.execute("SELECT * FROM data_persona")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data_persona = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            return render(request, 'horario/Crear_horario.html',{'data': data,'data_ruta': data_ruta,'data_vehiculo':data_vehiculo,'data_persona':data_persona})
