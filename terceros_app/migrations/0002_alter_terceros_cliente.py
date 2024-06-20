# Generated by Django 4.2.4 on 2024-06-11 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0001_initial'),
        ('terceros_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terceros',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes_app.clientes', verbose_name='Cliente'),
        ),
    ]