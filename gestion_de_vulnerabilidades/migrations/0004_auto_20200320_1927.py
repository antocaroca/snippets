# Generated by Django 3.0.4 on 2020-03-20 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_de_vulnerabilidades', '0003_auto_20200319_1427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vulnerabilidad',
            options={'ordering': ['created'], 'verbose_name': 'Vulnerabilidad', 'verbose_name_plural': 'Vulnerabilidades'},
        ),
    ]
