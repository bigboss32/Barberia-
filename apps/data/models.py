from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    duracion_estimada = models.IntegerField()
    servicio_solicitado = models.CharField(max_length=50)
    barbero_asignado = models.CharField(max_length=50)
    estado_cita = models.CharField(max_length=20)

class Barbero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    horario_trabajo = models.CharField(max_length=100)
    especialidades = models.CharField(max_length=100)

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

class Servicio(models.Model):
    tipo_servicio = models.CharField(max_length=50)
    descripcion = models.TextField()
    duracion_estimada = models.IntegerField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    productos = models.ManyToManyField(Producto, through='PrecioServicioProducto')

class PrecioServicioProducto(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Transaccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    total_transaccion = models.DecimalField(max_digits=10, decimal_places=2)
    detalles_transaccion = models.TextField()

class Retroalimentacion(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentarios = models.TextField()
