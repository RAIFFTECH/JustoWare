# Generated by Django 4.2.4 on 2024-02-03 04:48

from django.db import migrations, models
import django.db.models.deletion
import justo_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes_app', '0006_alter_clientes_fin_lic_alter_clientes_ini_lic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OFICINAS',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=5, verbose_name='Código Oficina')),
                ('contabiliza', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Contabiliza')),
                ('nombre_oficina', models.TextField(verbose_name='Nombre Oficina')),
                ('responsable', models.TextField(verbose_name='Responsable Oficina')),
                ('celular', models.CharField(help_text='El número de celular debe contener exactamente 10 dígitos numéricos.', max_length=10, null=True, validators=[justo_app.models.validate_numeric], verbose_name='Celular')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes_app.clientes', verbose_name='Cliente')),
            ],
            options={
                'db_table': 'oficinas',
                'unique_together': {('cliente', 'codigo')},
            },
        ),
    ]