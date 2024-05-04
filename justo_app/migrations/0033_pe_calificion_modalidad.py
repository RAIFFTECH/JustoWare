# Generated by Django 4.2.4 on 2024-02-24 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0032_clientes_clase_coop_pe_calificion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pe_calificion',
            name='modalidad',
            field=models.CharField(choices=[('CCCL', 'Consumo Con Libranza'), ('CCSL', 'Consumo sin Libranza'), ('CCPJ', 'Comercial Juridica'), ('CCPN', 'Comercial Natural'), ('CMIC', 'MicroCredito')], default='CCSL', max_length=6),
        ),
    ]