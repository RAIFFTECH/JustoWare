# Generated by Django 4.2.4 on 2024-02-21 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ctas_ahorros_app', '0001_initial'),
        ('lineas_ahorro_app', '0001_initial'),
        ('oficinas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctas_ahorro',
            name='lin_aho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lineas_ahorro_app.lineas_ahorro', verbose_name='Línea de Ahorro'),
        ),
        migrations.AddField(
            model_name='ctas_ahorro',
            name='oficina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficinas_app.oficinas', verbose_name='Oficina'),
        ),
        migrations.AlterUniqueTogether(
            name='ctas_ahorro',
            unique_together={('oficina', 'num_cta')},
        ),
    ]