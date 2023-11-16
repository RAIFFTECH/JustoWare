# Generated by Django 4.2.4 on 2023-11-10 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0016_alter_originacion_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociados',
            name='oficina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='justo_app.oficinas'),
        ),
        migrations.AlterField(
            model_name='asociados',
            name='tercero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='justo_app.terceros'),
        ),
    ]
