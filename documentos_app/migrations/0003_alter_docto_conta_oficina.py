# Generated by Django 4.2.4 on 2024-06-11 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficinas_app', '0001_initial'),
        ('documentos_app', '0002_xdoc_zep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docto_conta',
            name='oficina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oficinas_app.oficinas', verbose_name='Oficina'),
        ),
    ]