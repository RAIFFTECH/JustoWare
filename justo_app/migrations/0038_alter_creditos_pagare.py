# Generated by Django 5.0 on 2023-12-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0037_alter_creditos_num_pol_gar_hip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditos',
            name='pagare',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
