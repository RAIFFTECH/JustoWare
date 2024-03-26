# Generated by Django 4.2.4 on 2024-03-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0048_gar_no_idonea_delete_codeudores'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='gar_no_idonea',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='gar_no_idonea',
            name='doc_ide',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterUniqueTogether(
            name='gar_no_idonea',
            unique_together={('oficina', 'credito', 'doc_ide')},
        ),
        migrations.RemoveField(
            model_name='gar_no_idonea',
            name='tercero',
        ),
    ]
