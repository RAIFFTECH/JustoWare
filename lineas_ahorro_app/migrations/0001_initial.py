# Generated by Django 4.2.4 on 2024-02-21 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes_app', '0006_alter_clientes_fin_lic_alter_clientes_ini_lic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LINEAS_AHORRO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_lin_aho', models.CharField(max_length=2, null=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=30, null=True, verbose_name='Línea Ahorro')),
                ('termino', models.CharField(choices=[('D', 'Definido'), ('I', 'Indefinido')], max_length=1, verbose_name='Termino')),
                ('per_liq_int', models.CharField(choices=[('D', 'Diario'), ('M', 'Mensual'), ('C', 'Cdat'), ('V', 'Vencimiento')], max_length=1, verbose_name='Periodo Liquidación')),
                ('cta_por_pas', models.CharField(max_length=10, null=True, verbose_name='Cuenta Abono Intereses')),
                ('fec_ult_liq_int', models.DateField(blank=True, null=True, verbose_name='Última Liquidación Intereses')),
                ('saldo_minimo', models.FloatField(blank=True, null=True, verbose_name='Saldo Mínimo')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes_app.clientes', verbose_name='Cliente')),
            ],
            options={
                'db_table': 'lineas_ahorro',
                'unique_together': {('cliente', 'cod_lin_aho')},
            },
        ),
    ]