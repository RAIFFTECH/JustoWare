# Generated by Django 4.2.4 on 2024-02-14 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0008_creditos_cat_his_creditos_ca_oficina_f1ef77_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='CATE_INTE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('cod_cre', models.CharField(max_length=10, null=True)),
                ('tipo', models.CharField(max_length=1, null=True)),
                ('nit', models.CharField(max_length=12, null=True)),
                ('cod_ic_ini', models.CharField(max_length=2, null=True)),
                ('cod_ic_fin', models.CharField(max_length=2, null=True)),
                ('cat_ini', models.CharField(max_length=1, null=True)),
                ('cat_fin', models.CharField(max_length=1, null=True)),
                ('arr_ini', models.CharField(max_length=1, null=True)),
                ('arr_fin', models.CharField(max_length=1, null=True)),
                ('plazo', models.SmallIntegerField(null=True)),
                ('sal_cap_ini', models.FloatField(blank=True, null=True)),
                ('sal_cap_fin', models.FloatField(blank=True, null=True)),
                ('int_dia_ini', models.FloatField(blank=True, null=True)),
                ('int_cau_ini', models.FloatField(blank=True, null=True)),
                ('inicio', models.FloatField(blank=True, null=True)),
                ('int_pag', models.FloatField(blank=True, null=True)),
                ('int_dia_fin', models.FloatField(blank=True, null=True)),
                ('int_cau_fin', models.FloatField(blank=True, null=True)),
                ('final', models.FloatField(blank=True, null=True)),
                ('int_cau_mes', models.FloatField(blank=True, null=True)),
                ('int_pag_ant', models.FloatField(blank=True, null=True)),
                ('int_pag_act', models.FloatField(blank=True, null=True)),
                ('int_pag_ade', models.FloatField(blank=True, null=True)),
                ('ip_ant_A', models.FloatField(blank=True, null=True)),
                ('ip_ant_B', models.FloatField(blank=True, null=True)),
                ('ip_ant_C', models.FloatField(blank=True, null=True)),
                ('ip_ant_D', models.FloatField(blank=True, null=True)),
                ('ip_ant_E', models.FloatField(blank=True, null=True)),
                ('ip_ant_Z', models.FloatField(blank=True, null=True)),
                ('ip_ant_ZC', models.FloatField(blank=True, null=True)),
                ('ip_ant_ZD', models.FloatField(blank=True, null=True)),
                ('ip_ant_ZE', models.FloatField(blank=True, null=True)),
                ('ip_ant_ZF', models.FloatField(blank=True, null=True)),
                ('cue_pr_cob_A', models.FloatField(blank=True, null=True)),
                ('cue_pr_cob_B', models.FloatField(blank=True, null=True)),
                ('cue_pr_cob_C', models.FloatField(blank=True, null=True)),
                ('cue_pr_cob_D', models.FloatField(blank=True, null=True)),
                ('cue_pr_cob_E', models.FloatField(blank=True, null=True)),
                ('cue_pr_cob_F', models.FloatField(blank=True, null=True)),
                ('cau_ZC', models.FloatField(blank=True, null=True)),
                ('cau_ZD', models.FloatField(blank=True, null=True)),
                ('cau_ZE', models.FloatField(blank=True, null=True)),
                ('cau_ZF', models.FloatField(blank=True, null=True)),
                ('cau_ZET', models.FloatField(blank=True, null=True)),
                ('ingreso', models.FloatField(blank=True, null=True)),
                ('cue_por_pag', models.FloatField(blank=True, null=True)),
                ('cre_con_cas', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1)),
                ('int_con', models.FloatField(blank=True, null=True)),
                ('pro_ind_ini', models.FloatField(blank=True, null=True)),
                ('pro_ind_fin', models.FloatField(blank=True, null=True)),
                ('gas_pro_ind_ini', models.FloatField(blank=True, null=True)),
                ('gas_pro_ind_fin', models.FloatField(blank=True, null=True)),
                ('pro_gen_ini', models.FloatField(blank=True, null=True)),
                ('pro_gen_fin', models.FloatField(blank=True, null=True)),
                ('gas_gen_ind_ini', models.FloatField(blank=True, null=True)),
                ('gas_gen_ind_fin', models.FloatField(blank=True, null=True)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='justo_app.oficinas')),
            ],
            options={
                'db_table': 'cate_inte',
                'unique_together': {('oficina', 'fecha', 'cod_cre')},
            },
        ),
    ]
