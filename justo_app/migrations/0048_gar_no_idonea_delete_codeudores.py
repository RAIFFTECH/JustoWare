# Generated by Django 4.2.4 on 2024-03-03 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0047_creditos_tip_gar'),
    ]

    operations = [
        migrations.CreateModel(
            name='GAR_NO_IDONEA',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(default='C', max_length=1)),
                ('credito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='justo_app.creditos')),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='justo_app.oficinas')),
                ('tercero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='justo_app.terceros')),
            ],
            options={
                'db_table': 'gar_no_idonea',
                'unique_together': {('oficina', 'credito', 'tercero')},
            },
        ),
        migrations.DeleteModel(
            name='CODEUDORES',
        ),
    ]
