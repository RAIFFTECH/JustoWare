# Generated by Django 4.2.4 on 2024-02-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0015_alter_creditos_cat_his_arrastre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditos_cat_his',
            name='cat_int_mes',
            field=models.CharField(default=' ', max_length=1, null=True),
        ),
    ]