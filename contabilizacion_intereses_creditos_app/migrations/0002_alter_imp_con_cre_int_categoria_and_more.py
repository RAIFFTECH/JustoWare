# Generated by Django 4.2.4 on 2024-04-19 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0007_clientes_clase_coop_alter_clientes_id'),
        ('contabilizacion_intereses_creditos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imp_con_cre_int',
            name='categoria',
            field=models.CharField(choices=[('A', 'Normal'), ('B', 'Apreciable'), ('C', 'En Peligro'), ('D', 'En Mora'), ('E', 'Irrecuperable'), ('F', 'Castigado')], max_length=1, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='imp_con_cre_int',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes_app.clientes', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='imp_con_cre_int',
            name='cod_imp',
            field=models.CharField(max_length=2, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='imp_con_cre_int',
            name='cta_int',
            field=models.CharField(max_length=10, null=True, verbose_name='Cuenta Intereses'),
        ),
        migrations.AlterField(
            model_name='imp_con_cre_int',
            name='cta_ord_int',
            field=models.CharField(max_length=10, null=True, verbose_name='Cuenta de Orden Intereses'),
        ),
        migrations.AlterField(
            model_name='imp_con_cre_int',
            name='kcta_con',
            field=models.CharField(max_length=10, null=True, verbose_name='Cuenta Contable'),
        ),
        migrations.AlterField(
            model_name='imp_con_cre_int',
            name='kcta_pro_ind',
            field=models.CharField(max_length=10, null=True, verbose_name='Cuenta Provisión Individual'),
        ),
        migrations.AlterField(
            model_name='imp_con_cre_int',
            name='kporcentaje',
            field=models.FloatField(blank=True, null=True, verbose_name='Porcentaje'),
        ),
    ]
