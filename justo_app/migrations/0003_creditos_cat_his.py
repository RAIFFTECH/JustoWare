# Generated by Django 4.2.4 on 2024-02-12 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0002_delete_comprobantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CREDITOS_CAT_HIS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('cod_cre', models.CharField(max_length=10, null=True)),
                ('nit', models.CharField(max_length=12, null=True)),
                ('cod_lin_cre', models.CharField(max_length=2, null=True)),
                ('cod_imp_con', models.CharField(max_length=2, null=True)),
                ('for_pag', models.CharField(max_length=1, null=True)),
                ('plazo', models.SmallIntegerField(null=True)),
                ('dias_mor', models.SmallIntegerField(null=True)),
                ('cap_ini', models.FloatField(blank=True, null=True)),
                ('sal_cap', models.FloatField(blank=True, null=True)),
                ('sal_cap_dia', models.FloatField(blank=True, null=True)),
                ('sal_int_dia', models.FloatField(blank=True, null=True)),
                ('int_cau_res_per', models.FloatField(blank=True, null=True)),
                ('categoria', models.CharField(max_length=1, null=True)),
                ('arrastre', models.CharField(max_length=1, null=True)),
                ('aporte', models.FloatField(blank=True, null=True)),
                ('pro_ind', models.FloatField(blank=True, null=True)),
                ('saldo_1', models.FloatField(blank=True, null=True)),
                ('saldo_2', models.FloatField(blank=True, null=True)),
                ('vr_gar_hip', models.FloatField(blank=True, null=True)),
                ('cat_int_mes', models.CharField(max_length=1, null=True)),
                ('sal_cat_int', models.FloatField(blank=True, null=True)),
                ('castigo', models.CharField(max_length=1, null=True)),
                ('gas_pro_ind', models.FloatField(blank=True, null=True)),
                ('gas_pro_gen', models.FloatField(blank=True, null=True)),
                ('int_cor_per', models.FloatField(blank=True, null=True)),
                ('cat_mod', models.CharField(max_length=1, null=True)),
                ('cat_eva', models.CharField(max_length=1, null=True)),
                ('cat_ree', models.CharField(max_length=1, null=True)),
                ('cat_sel', models.CharField(max_length=1, null=True)),
                ('zeta', models.FloatField(blank=True, null=True)),
                ('puntaje', models.FloatField(blank=True, null=True)),
                ('pro_inc', models.FloatField(blank=True, null=True)),
                ('pdi', models.FloatField(blank=True, null=True)),
                ('vea', models.FloatField(blank=True, null=True)),
                ('per_esp', models.FloatField(blank=True, null=True)),
                ('conta_per', models.SmallIntegerField(null=True)),
                ('ali_cuota', models.SmallIntegerField(null=True)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='justo_app.oficinas')),
            ],
            options={
                'db_table': 'creditos_cat_his',
                'unique_together': {('oficina', 'fecha', 'cod_cre')},
            },
        ),
    ]
