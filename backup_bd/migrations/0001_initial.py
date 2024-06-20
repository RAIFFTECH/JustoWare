# Generated by Django 4.2.4 on 2024-05-07 16:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('filename', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'backup',
                'unique_together': {('timestamp',)},
            },
        ),
    ]