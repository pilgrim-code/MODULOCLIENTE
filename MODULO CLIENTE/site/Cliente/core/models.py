from statistics import mode
from django.db import models

# Create your models here.

# Tabla Cliente
class cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del cliente')
    telefono = models.IntegerField(verbose_name='Telefono')
    correo = models.CharField(max_length=100, verbose_name='Correo electronico')

#Tabla Carta
class carta(models.Model):
    id_carta = models.AutoField(primary_key=True)
    nombre_carta = models.CharField(max_length=100, verbose_name='Nombre')
    precio = models.IntegerField(verbose_name='Telefono')

#Tabla Boleta
class boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    medio_pago = models.CharField(max_length=100, verbose_name='Medio de pago')
    telefono = models.IntegerField(verbose_name='Telefono')
    correo = models.CharField(max_length=100, verbose_name='Correo electronico')

#Tabla Mesa
# class mesa(models.Model):
#     id_mesa = models.AutoField(primary_key=True)
#     cantidad_personas = models.IntegerField(verbose_name='Cantidad')
#     estado = models.CharField(max_length=3, verbose_name='Nombre del cliente')
#     reserva_id_reserva = models.IntegerField(verbose_name='Telefono')
#     correo = models.CharField(max_length=100, verbose_name='Correo electronico')
