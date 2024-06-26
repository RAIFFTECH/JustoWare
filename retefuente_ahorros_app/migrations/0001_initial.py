# Generated by Django 4.2.4 on 2024-03-11 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lineas_ahorro_app', '0002_alter_lineas_ahorro_cta_por_pas'),
    ]

    operations = [
        migrations.CreateModel(
            name='RET_FUE_AHO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicial', models.DateField(blank=True, null=True, verbose_name='Fecha Inicial')),
                ('fecha_final', models.DateField(blank=True, null=True, verbose_name='Fecha Final')),
                ('bas_liq_int', models.FloatField(blank=True, null=True, verbose_name='Base Liquidación Intereses')),
                ('tas_liq_rf', models.FloatField(blank=True, null=True, verbose_name='Tasa Liquidación Retefuente')),
                ('lin_aho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lineas_ahorro_app.lineas_ahorro', verbose_name='Línea Ahorro')),
            ],
            options={
                'db_table': 'RET_FUE_AHO',
                'unique_together': {('lin_aho', 'fecha_inicial')},
            },
        ),
    ]
