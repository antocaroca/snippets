# Generated by Django 3.0.4 on 2020-03-24 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_vulnerabilidades', '0004_auto_20200320_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vulnerabilidad',
            name='owner',
        ),
    ]
