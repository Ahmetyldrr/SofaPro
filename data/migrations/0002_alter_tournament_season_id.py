# Generated by Django 5.1.1 on 2024-09-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='season_id',
            field=models.IntegerField(unique=True, verbose_name='Sezon ID'),
        ),
    ]
