# Generated by Django 4.2.4 on 2024-03-15 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0054_ctas_ahorro_cod_imp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='int_dia_aho',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]