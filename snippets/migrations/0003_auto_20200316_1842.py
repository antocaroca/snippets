# Generated by Django 3.0.4 on 2020-03-16 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20200316_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventos_del_mes',
            old_name='anio',
            new_name='año',
        ),
    ]
