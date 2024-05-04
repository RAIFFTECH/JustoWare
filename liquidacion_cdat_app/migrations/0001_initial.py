# Generated by Django 4.2.4 on 2024-03-17 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ctas_ahorros_app', '0003_alter_ctas_ahorro_asociado'),
        ('hecho_economico_app', '0001_initial'),
        ('ampliacion_cdat_app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTA_CDAT_LIQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('tip_liq', models.CharField(choices=[('C', 'Causación Final'), ('D', 'Causación Diaria'), ('M', 'Causación Mensual'), ('V', 'Causación Vencimiento'), ('P', 'Pago')], max_length=1, verbose_name='Tipo Liquidación')),
                ('Val_int', models.FloatField(blank=True, null=True, verbose_name='Valor Intereses')),
                ('Val_ret', models.FloatField(blank=True, null=True, verbose_name='Valor Retefuente')),
                ('Val_ret_nue', models.FloatField(blank=True, null=True, verbose_name='Valor Retefuente Nueva')),
                ('aplicado', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Aplicado?')),
                ('cta_aho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctas_ahorros_app.ctas_ahorro', verbose_name='Cuenta de Ahorro')),
                ('cta_amp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ampliacion_cdat_app.cta_cdat_amp', verbose_name='Cuenta Ampliación')),
                ('docto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hecho_economico_app.hecho_econo', verbose_name='Número Documento')),
            ],
            options={
                'db_table': 'cta_cdat_liq',
                'unique_together': {('cta_aho', 'cta_amp', 'fecha', 'tip_liq')},
            },
        ),
    ]
