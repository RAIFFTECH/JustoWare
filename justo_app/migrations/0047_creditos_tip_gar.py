# Generated by Django 4.2.4 on 2024-03-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0046_rename_creditos_cat_his_carte_cat_his_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditos',
            name='tip_gar',
            field=models.CharField(choices=[('1', 'No Idonea'), ('2', 'Hipotecaria'), ('15', 'Sin Garantias')], default='15', max_length=2),
        ),
    ]