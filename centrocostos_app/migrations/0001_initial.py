# Generated by Django 4.2.4 on 2024-02-27 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oficinas_app', '0002_oficinas_ciudad_oficinas_direccion_alter_oficinas_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CENTROCOSTOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5, verbose_name='Código')),
                ('centro_costo', models.TextField(verbose_name='Centro de Costo')),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficinas_app.oficinas', verbose_name='Oficina')),
            ],
            options={
                'db_table': 'centro_costos',
                'unique_together': {('oficina', 'codigo')},
            },
        ),
    ]
