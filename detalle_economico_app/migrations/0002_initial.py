# Generated by Django 4.2.4 on 2024-03-17 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('detalle_economico_app', '0001_initial'),
        ('detalle_producto_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_econo',
            name='detalle_prod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='detalle_producto_app.detalle_prod', verbose_name='Detalle Producto'),
        ),
    ]