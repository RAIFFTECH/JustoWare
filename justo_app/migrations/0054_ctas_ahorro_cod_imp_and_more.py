# Generated by Django 4.2.4 on 2024-03-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0053_int_dia_aho'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctas_ahorro',
            name='cod_imp',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='cta_aho_est_his',
            name='est_cta_ant',
            field=models.CharField(choices=[('A', 'Activa'), ('C', 'Cancelada'), ('E', 'Embargada')], max_length=1),
        ),
        migrations.AlterField(
            model_name='ctas_ahorro',
            name='est_cta',
            field=models.CharField(choices=[('A', 'Activa'), ('C', 'Cancelada'), ('E', 'Embargada')], max_length=1),
        ),
    ]
