# Generated by Django 4.2.4 on 2024-01-12 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0002_alter_clientes_doc_ide_alter_clientes_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='fin_licencia',
            new_name='fin_lic',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='inicio_licencia',
            new_name='ini_lic',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='licencia_activa',
            new_name='lic_act',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='numero_licencia',
            new_name='num_lic',
        ),
    ]
