# Generated by Django 4.0.3 on 2022-04-04 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
                ('comprado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('sucursal', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('cargo', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
                ('entregado', models.BooleanField()),
            ],
        ),
    ]
