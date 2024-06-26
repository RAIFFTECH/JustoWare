# Generated by Django 4.2.4 on 2024-01-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0005_alter_clientes_doc_ide_alter_clientes_fin_lic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='fin_lic',
            field=models.DateField(verbose_name='Fecha Fin Licencia'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='ini_lic',
            field=models.DateField(verbose_name='Fecha Incio Licencia'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='num_lic',
            field=models.CharField(max_length=8, verbose_name='Número Licencia'),
        ),
    ]
