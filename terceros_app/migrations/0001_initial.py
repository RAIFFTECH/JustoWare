# Generated by Django 4.2.4 on 2024-02-03 04:18

from django.db import migrations, models
import django.db.models.deletion
import justo_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('localidades_app', '0001_initial'),
        ('clientes_app', '0006_alter_clientes_fin_lic_alter_clientes_ini_lic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TERCEROS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cla_doc', models.CharField(choices=[('C', 'Cédula de Ciudadanía'), ('T', 'Tarjeta de Identidad'), ('N', 'Nit'), ('R', 'Registro Civil'), ('E', 'Cédula de Extranjería'), ('P', 'Pasaporte'), ('O', 'Otros')], max_length=1)),
                ('doc_ide', models.CharField(max_length=12)),
                ('dig_ver', models.CharField(max_length=1, null=True)),
                ('nit_rap', models.CharField(max_length=12, null=True)),
                ('regimen', models.CharField(choices=[('48', 'Responsable'), ('49', 'No Responsable'), ('Comun', 'Común')], max_length=12)),
                ('fec_exp_ced', models.DateField(blank=True, null=True)),
                ('tip_ter', models.CharField(choices=[('N', 'Persona Natural'), ('J', 'Persona Jurídica'), ('O', 'Otro')], max_length=12)),
                ('pri_ape', models.CharField(max_length=28, null=True)),
                ('seg_ape', models.CharField(max_length=28, null=True)),
                ('pri_nom', models.CharField(max_length=28, null=True)),
                ('seg_nom', models.CharField(max_length=28, null=True)),
                ('raz_soc', models.CharField(max_length=120, null=True)),
                ('direccion', models.CharField(max_length=80, null=True)),
                ('cod_pos', models.CharField(max_length=8, null=True)),
                ('tel_ofi', models.CharField(max_length=10, null=True)),
                ('tel_res', models.CharField(max_length=10, null=True)),
                ('id_ds', models.BigIntegerField(db_index=True, null=True)),
                ('celular1', models.CharField(help_text='El número de celular debe contener exactamente 10 dígitos numéricos.', max_length=10, null=True, validators=[justo_app.models.validate_numeric])),
                ('celular2', models.CharField(max_length=10, null=True)),
                ('fax', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(blank=True, max_length=120, null=True)),
                ('fec_act', models.DateField(blank=True, null=True)),
                ('observacion', models.CharField(max_length=255, null=True)),
                ('per_pub_exp', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1)),
                ('nit_interno', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes_app.clientes')),
                ('cod_ciu_exp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ciu_exp', to='localidades_app.localidades')),
                ('cod_ciu_res', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ciu_res', to='localidades_app.localidades')),
            ],
            options={
                'db_table': 'terceros',
                'unique_together': {('cliente', 'cla_doc', 'doc_ide')},
            },
        ),
    ]