# Generated by Django 4.2.4 on 2024-02-12 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0005_creditos_cat_his_credito_creditos_cat_det'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='creditos_cat_det',
            unique_together={('oficina', 'fecha', 'cod_cre', 'fec_ref')},
        ),
    ]
