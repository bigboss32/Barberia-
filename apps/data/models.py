from django.db import models


class Estado(models.Model):
    descripcion_estado= models.CharField()

class Servicio(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    servicio= models.CharField()

class Departamento(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    nombre=models.CharField()

class Ciudad(models.Model):
    id_departamento= models.ForeignKey(Departamento, on_delete=models.CASCADE)
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    nombre=models.CharField()

class Persona(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    nombres=models.CharField()
    apellidos=models.CharField()
    direccion=models.CharField()
    telefono=models.IntegerField(unique=True)
    email=models.CharField(unique=True)

class TipoDocumento(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    tipo_documento=models.CharField()

class DocumentoPersona(models.Model):
    id_persona= models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_documento= models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    numero_documento=models.IntegerField()
    categoria_documento=models.CharField()

class DocumentoVehiculo(models.Model):
    id_tipodocumento=models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    fecha_tramite = models.DateField()
    fecha_expiracion = models.DateField()
    vigente=models.BooleanField()

class Marca(models.Model):
    marca=models.CharField()

class Color(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    color=models.CharField()

class Carroceria(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    nombre_carroceria=models.CharField()
    carro_detalle=models.CharField()

class Ruta(models.Model): 
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)

class RutaCiudad(models.Model):
    id_ruta=models.ForeignKey(Ruta, on_delete=models.CASCADE)
    id_ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    tiempoparada=models.IntegerField()

class Propetario(models.Model):
    id_persona= models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    fecha_afiliacion = models.DateField()

class Terminal(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_ciudad= models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    codigoterminal=models.CharField()

class Vehiculo(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_documentovehiculo=models.ForeignKey(DocumentoVehiculo, on_delete=models.CASCADE)
    id_marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    id_propietario=models.ForeignKey(Propetario, on_delete=models.CASCADE)
    id_color=models.ForeignKey(Color, on_delete=models.CASCADE)
    id_carroceria=models.ForeignKey(Carroceria, on_delete=models.CASCADE)
    id_ruta=models.ForeignKey(Ruta, on_delete=models.CASCADE)
    id_termina=models.ForeignKey(Terminal, on_delete=models.CASCADE)
    placa=models.CharField()
    cilindraje=models.IntegerField()
    numerochasis=models.IntegerField(unique=True)
    modelo=models.CharField()
    kilogramos=models.IntegerField()
    linea=models.CharField()


class Cliente(models.Model):
    id_persona= models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    fecha_registro = models.DateField()

class Conductor(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_vehiculo=models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    id_persona=models.ForeignKey(Persona, on_delete=models.CASCADE)
    fechainciotrabajo = models.DateField()
    experiencia=models.IntegerField()

class Usuario(models.Model):
    id_persona=models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    name=models.CharField()

class Rol(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    rol= models.CharField()

class UsuarioRol(models.Model):
    id_persona=models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_rol=models.ForeignKey(Rol, on_delete=models.CASCADE)
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    fecha_rol=models.DateField()

class Horario(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    diasemana=models.CharField()
    horaincio=models.TimeField()
    horafino=models.TimeField()

class HorarioConductor(models.Model):
    id_conductor=models.ForeignKey(Conductor, on_delete=models.CASCADE)
    id_horario=models.ForeignKey(Horario, on_delete=models.CASCADE)
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    fechaasignaconductor=models.DateField()

class Venta(models.Model):
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_ruta=models.ForeignKey(Ruta, on_delete=models.CASCADE)
    id_vehiculo=models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    ventafecha=models.DateField()
    totalneto=models.FloatField()
    totalbruto=models.FloatField()
    procentajedescuento=models.FloatField()

class Tiquete(models.Model):
    id_cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    id_venta= models.ForeignKey(Venta, on_delete=models.CASCADE)
    tiqvehiculo=models.CharField()
    puesto=models.IntegerField()
    totalbruto=models.FloatField()
    iva= models.FloatField()
    totalmasiva=models.FloatField()
    descuento=models.FloatField()






