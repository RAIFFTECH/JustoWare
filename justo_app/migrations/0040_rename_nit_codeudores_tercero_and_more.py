# Generated by Django 5.0 on 2023-12-25 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0039_codeudores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codeudores',
            old_name='nit',
            new_name='tercero',
        ),
        migrations.AlterUniqueTogether(
            name='codeudores',
            unique_together={('oficina', 'credito', 'tercero')},
        ),
    ]
