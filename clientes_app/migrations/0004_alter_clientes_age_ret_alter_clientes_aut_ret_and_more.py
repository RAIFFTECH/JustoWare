# Generated by Django 4.2.4 on 2024-01-12 20:52

from django.db import migrations, models
import justo_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0003_rename_fin_licencia_clientes_fin_lic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='age_ret',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Agente Retención'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='aut_ret',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Autorretenedor'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='celular',
            field=models.CharField(help_text='El número de celular debe contener exactamente 10 dígitos numéricos.', max_length=10, null=True, validators=[justo_app.models.validate_numeric], verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='ciudad',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='codigo',
            field=models.CharField(max_length=1, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='doc_ide',
            field=models.CharField(help_text='El documento de identidad debe ser numérico.', max_length=12, null=True, validators=[justo_app.models.validate_numeric], verbose_name='Nit'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='dominio',
            field=models.URLField(verbose_name='Dominio'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='dv',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='DV'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fin_lic',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Fin Licencia'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='ini_lic',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Incio Licencia'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='lic_act',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Licencia Activa'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='logo',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to='', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nit_con',
            field=models.CharField(blank=True, help_text='El número de documento debe ser numérico.', max_length=10, null=True, validators=[justo_app.models.validate_numeric], verbose_name='Documento Contador'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nit_ger',
            field=models.CharField(blank=True, help_text='El número de documento debe ser numérico.', max_length=10, null=True, validators=[justo_app.models.validate_numeric], verbose_name='Documento Gerente'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nit_rev_fis',
            field=models.CharField(blank=True, help_text='El número de documento debe ser numérico.', max_length=10, null=True, validators=[justo_app.models.validate_numeric], verbose_name='Documento Revisor Fiscal'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nom_con',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre Contador'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nom_ger',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre Gerente'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nom_rev_fis',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre Revisor Fiscal'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(max_length=120, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='num_lic',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Número Licencia'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='ret_iva',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1, verbose_name='Retiene Iva'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='sigla',
            field=models.CharField(max_length=36, verbose_name='Sigla'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(blank=True, help_text='El número de teléfono debe tener solo dígitos numéricos.', max_length=12, null=True, validators=[justo_app.models.validate_numeric], verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tp_con',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Tar. Prof. Contador'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tp_rev_fis',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Tar. Prof. Revisor'),
        ),
    ]