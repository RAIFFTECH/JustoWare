# Generated by Django 4.2.4 on 2024-02-19 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0028_rename_cod_ic_ini_cate_inte_cod_imp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cate_inte',
            name='cod_ic_fin',
        ),
        migrations.RemoveField(
            model_name='cate_inte',
            name='plazo',
        ),
    ]