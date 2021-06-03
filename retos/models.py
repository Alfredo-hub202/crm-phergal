from django.db import models
from django.http import request
from phone_field import PhoneField
from datetime import date


#  models Tipo de Retos.


class Tipo_retos(models.Model):
    description = models.TextField('description', blank=True, null=True)
    n_producto = models.IntegerField(
        'n_producto', blank=True, null=True)
    estado = models.BooleanField('estado', default=False)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return self.description


#  models marca.
class Marca(models.Model):
    nombre = models.CharField('nombre', max_length=255)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return self.nombre

    #  models gama.


class Gama(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField('nombre', max_length=255)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return self.nombre

    #  models Tipo_Producto.


class Tipo_producto(models.Model):
    nombre = models.CharField('nombre', max_length=255)
    orden_listado = models.IntegerField(
        'orden_listado', blank=True, null=True)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return self.nombre


#  models Productos.
class Productos(models.Model):
    gama = models.ForeignKey(Gama, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tipo_articulo = models.ForeignKey(
        Tipo_producto, on_delete=models.CASCADE)
    tipo_unidad = models.TextField('tipo_unidad', blank=True)
    nombre = models.CharField('nombre', max_length=255)
    description = models.TextField('description', blank=True)
    moneda = models.TextField('moneda', blank=True)
    activo_pedido = models.BooleanField('activo_pedido', default=False)
    activo_devolucion = models.BooleanField('activo_devolucion', default=False)
    es_medicamento = models.BooleanField('es_medicamento', default=False)
    cod_nacional = models.TextField('cod_nacional', blank=True)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return self.nombre

    #  models Retos Productos.


class Productos_retos(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    tipo_retos = models.ForeignKey(Tipo_retos, on_delete=models.CASCADE)
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return str(self.tipo_retos)

  #  models Regalos Productos.


class Productos_regalo(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    Tipo_retos = models.ForeignKey(Tipo_retos, on_delete=models.CASCADE)
    estado = models.BooleanField('estado', default=True)
    description = models.TextField('description', blank=True)
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return self.description

  # Models Forma_Pago


class Forma_pago(models.Model):
    nombre = models.CharField('nombre', max_length=255)
    seleccionable = models.IntegerField(
        'seleccionable', blank=True, null=True)
    necesita = models.IntegerField(
        'necesita', blank=True, null=True)
    iban = models.CharField('iban', max_length=255)
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return self.nombre

  # Models Tipo_Negocio


class Tipo_Negocio(models.Model):
    nombre = models.CharField('nombre', max_length=255)
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return self.nombre


#  models Empleados.
class Cliente(models.Model):
    cliente_codigo = models.CharField('cliente_codigo', max_length=255)
    forma_pago = models.ForeignKey(
        Forma_pago,
        on_delete=models.CASCADE)
    tipo_Negocio = models.ForeignKey(
        Tipo_Negocio,
        on_delete=models.CASCADE)
    nombre = models.CharField('nombre', max_length=255)
    apellido = models.CharField('apellido', max_length=255)
    clasificacion_global_ano_act = models.TextField(
        'clasificacion_global_ano_act', blank=True)
    facturacion_ano_ant = models.TextField('facturacion_ano_ant', blank=True)
    clasificacion_potencial = models.TextField(
        'clasificacion_potencial', blank=True)
    acuerdo = models.TextField('acuerdo', blank=True)
    nif = models.TextField('nif', blank=True)
    bloqueado = models.BooleanField('bloqueado', default=True)
    grupo_compra = models.TextField('grupo_compra', blank=True)
    clasificacion_global_ano_ant = models.TextField(
        'clasificacion_global_ano_ant', blank=True)
    facturacion_ano_act = models.TextField('facturacion_ano_act', blank=True)
    acepta_el_contrato = models.BooleanField(
        'acepta_el_contrato', default=True)
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return self.nombre


#  models Empleados.
class Empleados(models.Model):
    nombre = models.CharField('nombre', max_length=255)
    apellido = models.CharField('apellido', max_length=255)
    telefono = PhoneField(blank=True, help_text='Telefono de Contacto')
    fecha_nacimiento = models.DateField('fecha_nacimiento', null=True)
    email = models.EmailField('email', blank=True)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return self.nombre


#  models Cliente Retos.

class Cliente_retos(models.Model):
    nombre = models.CharField('nombre', max_length=255)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE)
    tipos_retos = models.ForeignKey(
        Tipo_retos, on_delete=models.CASCADE)
    firma = models.BooleanField('Firma', default=True)
    fecha_ini = models.DateField('Fecha Inicio', null=True)
    fecha_fin = models.DateField('Fecha Fin', null=True)
    max_venta = models.BigIntegerField('Maximo de Ventas')
    n_ventas_activas = models.BigIntegerField('Numero de ventas activas')
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)
    estado = models.BooleanField('estado', default=True)

    def __str__(self):
        return self.nombre


class Cli_retos_art(models.Model):
    n_ticket = models.CharField('Nº Ticket', max_length=255)
    images = models.ImageField(upload_to='images', verbose_name='Imágen')
    validar_foto = models.BooleanField('Validar', default=False)
    clave_reto_farmacia = models.CharField('Clave', max_length=255)
    date = date.today()
    fecha_alta = models.DateField('Fecha Alta', default=date)
    cliente_reto = models.ForeignKey(
        Cliente_retos, on_delete=models.CASCADE)
    Productos = models.ForeignKey(
        Productos, on_delete=models.CASCADE)
    productos_regalo = models.ForeignKey(
        Productos_regalo, on_delete=models.CASCADE)

    def __str__(self):
        return self.n_ticket
