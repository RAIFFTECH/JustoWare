# Generated by Django 4.2.4 on 2024-02-17 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0024_rename_orden_i_imp_con_cre_kic_orden_i'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imp_con_cre',
            old_name='k_pte_ic',
            new_name='kpte_ic',
        ),
    ]