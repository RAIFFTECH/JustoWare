# Generated by Django 4.2.4 on 2024-04-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilizacion_capital_creditos_app', '0002_remove_imp_con_cre_icta_des_int_pp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imp_con_cre',
            name='kcta_ingreso',
            field=models.CharField(max_length=10, null=True, verbose_name='Cuenta Ingresos'),
        ),
        migrations.AlterField(
            model_name='imp_con_cre',
            name='kdet_gen_gas',
            field=models.CharField(max_length=10, null=True, verbose_name='Cuenta Gasto Provisión'),
        ),
    ]