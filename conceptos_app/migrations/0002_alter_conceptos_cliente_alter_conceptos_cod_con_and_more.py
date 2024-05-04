# Generated by Django 4.2.4 on 2024-03-30 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0007_clientes_clase_coop_alter_clientes_id'),
        ('conceptos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conceptos',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes_app.clientes', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='cod_con',
            field=models.CharField(max_length=8, verbose_name='Código Concepto'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='con_justo',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Concepto Justo'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='credito',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Concepto Crédito?'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='cta_con',
            field=models.CharField(max_length=10, verbose_name='Cuenta Contable'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='cta_con_pas',
            field=models.CharField(max_length=10, verbose_name='Cuenta Contable Pasivo'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='debito',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Concepto Débito?'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='descripcion',
            field=models.CharField(max_length=44, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='por_ret_fue',
            field=models.FloatField(blank=True, null=True, verbose_name='Usa Retefuente?'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='por_tercero',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Usa Tercero?'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='tip_con',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Tipo Concepto'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='tip_dev_ap',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Tipo Devolución Aportes'),
        ),
        migrations.AlterField(
            model_name='conceptos',
            name='tip_sis',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Tipo Sistema'),
        ),
    ]