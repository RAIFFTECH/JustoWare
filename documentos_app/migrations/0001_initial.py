# Generated by Django 4.2.4 on 2024-02-27 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oficinas_app', '0002_oficinas_ciudad_oficinas_direccion_alter_oficinas_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='DOCTO_CONTA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_con', models.IntegerField(blank=True, null=True, verbose_name='Periodo Contable')),
                ('codigo', models.IntegerField(verbose_name='Código Documento')),
                ('nom_cto', models.CharField(max_length=12, verbose_name='Nombre Corto')),
                ('nombre', models.CharField(max_length=44, verbose_name='Nombre Documento')),
                ('doc_admin', models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=1, null=True, verbose_name='Documento Administrativo?')),
                ('doc_caja', models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=1, null=True, verbose_name='Documento de Caja?')),
                ('inicio_nuevo_per', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Reinicia Numeración?')),
                ('consecutivo', models.IntegerField(blank=True, null=True, verbose_name='Consecutivo')),
                ('id_ds', models.BigIntegerField(blank=True, db_index=True, null=True)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficinas_app.oficinas', verbose_name='Oficina')),
            ],
            options={
                'db_table': 'docto_conta',
                'unique_together': {('oficina', 'per_con', 'codigo')},
            },
        ),
    ]