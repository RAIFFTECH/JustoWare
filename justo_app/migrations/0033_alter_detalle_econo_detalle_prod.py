# Generated by Django 5.0 on 2023-12-25 01:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0032_alter_hecho_econo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_econo',
            name='detalle_prod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='justo_app.detalle_prod'),
        ),
    ]
