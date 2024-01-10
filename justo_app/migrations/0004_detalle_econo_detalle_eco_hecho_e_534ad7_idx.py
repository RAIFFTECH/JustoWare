# Generated by Django 4.2.4 on 2024-01-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0003_alter_detalle_econo_unique_together'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='detalle_econo',
            index=models.Index(fields=['hecho_econo', 'cuenta', 'tercero', 'detalle_prod'], name='detalle_eco_hecho_e_534ad7_idx'),
        ),
    ]