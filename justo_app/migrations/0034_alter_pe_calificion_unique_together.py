# Generated by Django 4.2.4 on 2024-02-24 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0033_pe_calificion_modalidad'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pe_calificion',
            unique_together={('cliente', 'clase_coop', 'modalidad', 'calificacion')},
        ),
    ]