# Generated by Django 4.2.4 on 2024-02-19 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0027_rename_val_ali_creditos_cat_det_val_det_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cate_inte',
            old_name='cod_ic_ini',
            new_name='cod_imp',
        ),
    ]
