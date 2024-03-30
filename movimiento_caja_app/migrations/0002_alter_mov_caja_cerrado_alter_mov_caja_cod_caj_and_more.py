# Generated by Django 4.2.4 on 2024-03-30 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficinas_app', '0002_oficinas_ciudad_oficinas_direccion_alter_oficinas_id'),
        ('movimiento_caja_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mov_caja',
            name='cerrado',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Cierre de Caja?'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='cod_caj',
            field=models.CharField(max_length=2, verbose_name='Código Cajero'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='creditos',
            field=models.FloatField(blank=True, null=True, verbose_name='Movimientos Créditos'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='debitos',
            field=models.FloatField(blank=True, null=True, verbose_name='Movimientos Débitos'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='diferencia',
            field=models.FloatField(blank=True, null=True, verbose_name='Diferencia'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='fecha',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='jornada',
            field=models.CharField(max_length=1, verbose_name='Jornada'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='monedas',
            field=models.JSONField(blank=True, null=True, verbose_name='Dinero en Efectivo'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='oficina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oficinas_app.oficinas', verbose_name='Oficina'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='saldo_fin',
            field=models.FloatField(blank=True, null=True, verbose_name='Saldo Final'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='saldo_ini',
            field=models.FloatField(blank=True, null=True, verbose_name='Saldo Inicial'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='val_che_dev',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor Cheques Devueltos'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='val_cheques',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor Cheques'),
        ),
        migrations.AlterField(
            model_name='mov_caja',
            name='val_vales',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor Vales'),
        ),
    ]
