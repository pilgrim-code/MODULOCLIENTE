# Generated by Django 4.0.6 on 2022-09-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('medio_pago', models.CharField(max_length=100, verbose_name='Medio de pago')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('correo', models.CharField(max_length=100, verbose_name='Correo electronico')),
            ],
        ),
        migrations.CreateModel(
            name='carta',
            fields=[
                ('id_carta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_carta', models.CharField(max_length=100, verbose_name='Nombre')),
                ('precio', models.IntegerField(verbose_name='Telefono')),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del cliente')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('correo', models.CharField(max_length=100, verbose_name='Correo electronico')),
            ],
        ),
    ]
