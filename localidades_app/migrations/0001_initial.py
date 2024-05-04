# Generated by Django 4.2.4 on 2024-02-03 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes_app', '0006_alter_clientes_fin_lic_alter_clientes_ini_lic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LOCALIDADES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8, verbose_name='Código')),
                ('nombre', models.CharField(max_length=36, verbose_name='Ciudad')),
                ('cod_pos', models.CharField(max_length=12, null=True, verbose_name='Código Postal')),
                ('departamento', models.CharField(max_length=36, null=True, verbose_name='Departamento')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes_app.clientes', verbose_name='Cliente')),
            ],
            options={
                'db_table': 'localidades',
                'unique_together': {('cliente', 'codigo')},
            },
        ),
    ]