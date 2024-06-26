# Generated by Django 4.2.4 on 2024-03-17 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes_app', '0006_alter_clientes_fin_lic_alter_clientes_ini_lic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMP_CON_CRE_INT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_imp', models.CharField(max_length=2, null=True)),
                ('categoria', models.CharField(choices=[('A', 'Normal'), ('B', 'Apreciable'), ('C', 'En Peligro'), ('D', 'En Mora'), ('E', 'Irrecuperable'), ('F', 'Castigado')], max_length=1)),
                ('kcta_con', models.CharField(max_length=10, null=True)),
                ('kcta_pro_ind', models.CharField(max_length=10, null=True)),
                ('kporcentaje', models.FloatField(blank=True, null=True)),
                ('cta_int', models.CharField(max_length=10, null=True)),
                ('cta_ord_int', models.CharField(max_length=10, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes_app.clientes')),
            ],
            options={
                'db_table': 'imp_con_cre_int',
                'unique_together': {('cliente', 'cod_imp', 'categoria')},
            },
        ),
    ]
