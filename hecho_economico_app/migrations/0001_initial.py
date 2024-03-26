# Generated by Django 4.2.4 on 2024-03-17 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documentos_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HECHO_ECONO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(blank=True, null=True, verbose_name='Número')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('descripcion', models.CharField(max_length=64, null=True, verbose_name='Descripción')),
                ('anulado', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Anulado?')),
                ('protegido', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Protegido?')),
                ('fecha_prot', models.DateTimeField(auto_now=True, verbose_name='Fecha Protegido')),
                ('usuario', models.CharField(max_length=16, null=True, verbose_name='Usuario')),
                ('canal', models.CharField(choices=[('ATM', 'Red de Cajeros'), ('POS', 'Compras en Comercios'), ('IVR', 'Audio Respuesta'), ('TRA', 'Transferencia'), ('CON', 'Consignación'), ('EFE', 'Efectivo'), ('CHE', 'Cheque'), ('GIR', 'Giro'), ('WEB', 'Portal Transaccional'), ('MOV', 'Banca Móvil'), ('OFI', 'Oficina'), ('CNB', 'Corresponsales Bancarios'), ('RAL', 'Redes Aliadas')], max_length=3, verbose_name='Canal')),
                ('id_ds', models.BigIntegerField(db_index=True, null=True, verbose_name='id_ds')),
                ('docto_conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos_app.docto_conta', verbose_name='Documento')),
            ],
            options={
                'db_table': 'hecho_econo',
                'unique_together': {('docto_conta', 'numero')},
            },
        ),
    ]
