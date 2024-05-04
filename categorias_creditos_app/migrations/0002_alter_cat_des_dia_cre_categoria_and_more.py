# Generated by Django 4.2.4 on 2024-03-30 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0007_clientes_clase_coop_alter_clientes_id'),
        ('categorias_creditos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat_des_dia_cre',
            name='categoria',
            field=models.CharField(choices=[('A', 'Normal'), ('B', 'Apreciable'), ('C', 'En Peligro'), ('D', 'En Mora'), ('E', 'Irrecuperable'), ('F', 'Castigado')], max_length=1, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='cat_des_dia_cre',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes_app.clientes', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='cat_des_dia_cre',
            name='codigo',
            field=models.IntegerField(verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='cat_des_dia_cre',
            name='maximo_dias',
            field=models.IntegerField(null=True, verbose_name='Máximo Días'),
        ),
        migrations.AlterField(
            model_name='cat_des_dia_cre',
            name='minimo_dias',
            field=models.IntegerField(null=True, verbose_name='Mínimo Días'),
        ),
    ]