# Generated by Django 3.0.4 on 2020-03-24 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_amenazas', '0006_auto_20200320_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alerta_amenaza',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='amenazas_del_mes',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='grafico_lineas_tendencia_amenazas',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='tendencia_amenaza',
            name='owner',
        ),
    ]
