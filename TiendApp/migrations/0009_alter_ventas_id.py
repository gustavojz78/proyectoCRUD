# Generated by Django 4.0.3 on 2022-04-05 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendApp', '0008_staff_puesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]