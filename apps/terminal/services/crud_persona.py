from django.db import connection
from collections import namedtuple
from django.shortcuts import render,redirect

class Persona():
    def crearpersona(self,request):

        if request.method == 'POST':
             nombre = request.POST['nombre']
             apellidos = request.POST['apellidos']
             dirreccion = request.POST['dirreccion']
             celular = request.POST['celular']
             correo = request.POST['correo']
             tipo_estado = request.POST['tipo_estado']
             Documento = request.POST['Documento']
             Ciudad = request.POST['Ciudad']
             numero_doc = request.POST['numero_doc']
             with connection.cursor() as cursor:
                 cursor.execute("INSERT INTO data_persona (nombres,apellidos,direccion,telefono,email,id_ciudad_id,id_estado_id) VALUES (%s, %s,%s, %s,%s, %s,%s)", 
                                [nombre, apellidos,dirreccion,celular,correo,Ciudad,tipo_estado])
                 cursor.execute("SELECT LASTVAL()")
                 id = cursor.fetchone()[0]
                 cursor.execute("INSERT INTO data_documentopersona (numero_documento,categoria_documento,id_persona_id,id_documento_id,id_estado_id) VALUES (%s, %s,%s, %s,%s)", 
                                [numero_doc, apellidos,id,Documento,tipo_estado])
                 
                 connection.commit()
                 return redirect('crear_persona')
    
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM data_estado")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data_estado = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            cursor.execute("SELECT * FROM data_departamento")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data_departamento = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            cursor.execute("SELECT * FROM data_ciudad")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data_ciudad = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            cursor.execute("SELECT * FROM data_tipodocumento")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data_doc = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            return render(request, 'persona/Crear_persona.html',{'data': data_estado,'data_departamento':data_departamento,'data_ciudad':data_ciudad,'data_Documento':data_doc})
    def creardocumento(self,request):
        
        if request.method == 'POST':
             nombre = request.POST['nombre']
             tipo_estado = request.POST['tipo_estado']
      
             with connection.cursor() as cursor:
                 cursor.execute("INSERT INTO data_tipodocumento (tipo_documento,id_estado_id) VALUES (%s, %s)", 
                                [nombre,tipo_estado])
                 connection.commit()
                 return redirect('crear_documento')
    
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM data_estado")
            columnas = [col[0] for col in cursor.description]  # Nombres de columnas
            data_estado = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
            return render(request, 'documento/Crear_documento.html',{'data': data_estado})