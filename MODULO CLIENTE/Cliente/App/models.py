# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asignacion(models.Model):
    id_asignacion = models.BigIntegerField(primary_key=True)
    fecha_termino = models.DateField(blank=True, null=True)
    esta_permiso = models.CharField(max_length=1)
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')
    permiso_id_permiso = models.ForeignKey('Permiso', models.DO_NOTHING, db_column='permiso_id_permiso')

    class Meta:
        managed = False
        db_table = 'asignacion'


class Bodega(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    kg = models.FloatField(blank=True, null=True)
    lt = models.FloatField(blank=True, null=True)
    stock = models.BigIntegerField()
    ultima_repo = models.DateField()

    class Meta:
        managed = False
        db_table = 'bodega'


class Boleta(models.Model):
    id_boleta = models.BigIntegerField(primary_key=True)
    medio_pago = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'boleta'


class Carta(models.Model):
    id_carta = models.BigIntegerField(primary_key=True)
    nombre_carta = models.CharField(max_length=100)
    precio = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'carta'


class Cliente(models.Model):
    id_cliente = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.TextField(max_length=100, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'cliente'


class Detalle(models.Model):
    id_detalle = models.BigIntegerField(primary_key=True)
    cantidad = models.BigIntegerField()
    anotaciones = models.CharField(max_length=200, blank=True, null=True)
    extra = models.CharField(max_length=1)
    pedido_id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='pedido_id_pedido')
    carta_id_carta = models.ForeignKey(Carta, models.DO_NOTHING, db_column='carta_id_carta')

    class Meta:
        managed = False
        db_table = 'detalle'


class Ingredientes(models.Model):
    id_ingrediente = models.BigIntegerField(primary_key=True)
    bodega_id_producto = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_id_producto')
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ingredientes'


class Merma(models.Model):
    id_merma = models.BigIntegerField(primary_key=True)
    cantidad = models.BigIntegerField()
    fecha = models.DateField()
    bodega_id_producto = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_id_producto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merma'


class Mesa(models.Model):
    id_mesa = models.BigIntegerField(primary_key=True)
    cantidad_personas = models.BigIntegerField()
    estado = models.CharField(max_length=1)
    reserva_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesa'


class Orden(models.Model):
    id_orden = models.BigIntegerField(primary_key=True)
    nombre_orden = models.CharField(max_length=100)
    kg = models.FloatField(blank=True, null=True)
    lt = models.FloatField(blank=True, null=True)
    cantidad = models.BigIntegerField()
    fecha_orden = models.DateField()
    bodega_id_producto = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_id_producto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden'


class Pedido(models.Model):
    id_pedido = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    total = models.BigIntegerField()
    estado = models.CharField(max_length=1)
    mesa_id_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='mesa_id_mesa', blank=True, null=True)
    boleta_id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_id_boleta')
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class Permiso(models.Model):
    id_permiso = models.BigIntegerField(primary_key=True)
    nombre_permiso = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'permiso'


class Receta(models.Model):
    id_receta = models.BigIntegerField(primary_key=True)
    nombre_receta = models.CharField(max_length=100)
    carta_id_carta = models.ForeignKey(Carta, models.DO_NOTHING, db_column='carta_id_carta')
    ingredientes_id_ingrediente = models.ForeignKey(Ingredientes, models.DO_NOTHING, db_column='ingredientes_id_ingrediente')

    class Meta:
        managed = False
        db_table = 'receta'


class Reserva(models.Model):
    id_reserva = models.IntegerField(db_column='ID_RESERVA', primary_key=True)
    nombre_re = models.CharField(max_length=100)
    fecha = models.DateField()
    telefono = models.IntegerField(db_column='TELEFONO')
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva'


class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'