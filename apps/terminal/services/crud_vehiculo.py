
from django.db import connection
from collections import namedtuple
from django.shortcuts import render,redirect
class Vehiculo():
    def crearvehiculo(self,request):
       
        if request.method == 'POST':
            nombre_documento_vehi = request.POST.get('Documento_vehi', '')
            estado_documento_vehi = request.POST.get('tipo_estado_documento_vehi', '')
            fecha_tramite = request.POST.get('fecha_tramite', '')
            fecha_expiracion = request.POST.get('fecha_expiracion', '')
            vigente = request.POST.get('check', '')
            estado_carroceria = request.POST.get('tipo_estado_Carroceria', '')
            nombre_carroceria = request.POST.get('nombre_carroceria', '')
            carro_detalle = request.POST.get('carro_detalle', '')
            marca = request.POST.get('Marca', '')
            color = request.POST.get('Color', '')
            estado_ruta = request.POST.get('tipo_estado_ruta', '')
            ciudad_ruta = request.POST.get('Ciudad', '')
            hora_parada = request.POST.get('parada', '')
            data_persona = request.POST.get('data_persona', '')
            estado_propietario = request.POST.get('tipo_estado', '')
            fecha_tramite_pro = request.POST.get('fecha_tramite_pro', '')
            ciudad_terminal = request.POST.get('Ciudad', '')
            estado_terminal = request.POST.get('tipo_estado_terminal', '')
            codigo_terminal = request.POST.get('codigo_terminal', '')
            placa = request.POST.get('placa', '')
            cilindraje = request.POST.get('cilindraje', '')
            numerochasis = request.POST.get('numerochasis', '')
            modelo = request.POST.get('modelo', '')
            kilogramos = request.POST.get('kilogramos', '')
            linea = request.POST.get('linea', '')
            fechainciotrabajo=request.POST.get('fechainciotrabajo', '')
            Experiencia=request.POST.get('Experiencia', '')
            

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO data_documentovehiculo (id_tipodocumento_id,id_estado_id,fecha_tramite,fecha_expiracion,vigente) VALUES (%s, %s,%s, %s,%s)", 
                                [nombre_documento_vehi, estado_documento_vehi,fecha_tramite,fecha_expiracion,vigente])
                cursor.execute("SELECT LASTVAL()")
                id_data_documentovehiculo= cursor.fetchone()[0]
                cursor.execute("INSERT INTO data_marca (marca) VALUES (%s)", 
                                [marca])
                cursor.execute("SELECT LASTVAL()")
                id_marca= cursor.fetchone()[0]
                cursor.execute("INSERT INTO data_color (color,id_estado_id) VALUES (%s,%s)", 
                                [color,estado_carroceria])
                cursor.execute("SELECT LASTVAL()")
                id_color= cursor.fetchone()[0]
                
                cursor.execute("INSERT INTO data_carroceria(nombre_carroceria,carro_detalle,id_estado_id) VALUES (%s,%s,%s)", 
                                [nombre_carroceria,carro_detalle,estado_carroceria])
                cursor.execute("SELECT LASTVAL()")
                id_carroceria= cursor.fetchone()[0]
                cursor.execute("INSERT INTO data_propetario (id_persona_id,id_estado_id,fecha_afiliacion) VALUES (%s,%s,%s)", 
                                [data_persona,estado_propietario,fecha_tramite_pro])
                cursor.execute("SELECT LASTVAL()")
                id_propietario= cursor.fetchone()[0]
                cursor.execute("INSERT INTO data_terminal(id_ciudad_id,id_estado_id,codigoterminal) VALUES (%s,%s,%s)", 
                                [ciudad_terminal,estado_terminal,codigo_terminal])
                cursor.execute("SELECT LASTVAL()")
                id_terminal= cursor.fetchone()[0]
                cursor.execute("INSERT INTO data_ruta(id_estado_id) VALUES (%s)", 
                                [estado_ruta])
                cursor.execute("SELECT LASTVAL()")
                id_ruta= cursor.fetchone()[0]

                cursor.execute("INSERT INTO data_rutaciudad(id_estado_id,id_ruta_id,id_ciudad_id,tiempoparada) VALUES (%s,%s,%s,%s)", 
                                [estado_ruta,id_ruta,ciudad_ruta,hora_parada])
                cursor.execute("SELECT LASTVAL()")
                id_rutaciudad= cursor.fetchone()[0]
                cursor.execute("INSERT INTO data_vehiculo(placa,cilindraje,numerochasis,modelo,kilogramos,linea,id_estado_id,id_documentovehiculo_id,id_marca_id,id_propietario_id,id_color_id,id_carroceria_id,id_ruta_id,id_termina_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                                [placa,cilindraje,numerochasis,modelo,kilogramos,linea,estado_carroceria,id_data_documentovehiculo,
                                 id_marca,id_propietario,id_color,id_carroceria,id_ruta,id_terminal])
                cursor.execute("SELECT LASTVAL()")
                id_vehiculo= cursor.fetchone()[0]
                cursor.execute("INSERT INTO data_conductor(fechainciotrabajo,experiencia,id_persona_id,id_vehiculo_id,id_estado_id) VALUES (%s,%s,%s,%s,%s)", 
                                [fechainciotrabajo,Experiencia,data_persona,id_vehiculo,estado_carroceria])




                return redirect('crear_vehiculo')
         


        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM data_estado")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            cursor.execute("SELECT * FROM data_tipodocumento")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data_doc = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            cursor.execute("SELECT * FROM data_ciudad")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data_ciudad = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            cursor.execute("SELECT * FROM data_persona")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data_persona = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            return render(request, 'vehiculo/Crear_vehiculo.html',{'data': data,'data_Documento':data_doc,'data_ciudad':data_ciudad,'data_persona':data_persona})