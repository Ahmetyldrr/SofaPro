# Generated by Django 5.1.1 on 2024-09-21 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_id', models.IntegerField(verbose_name='Sezon ID')),
                ('tournament_id', models.IntegerField(verbose_name='Turnuva ID')),
                ('country_name', models.CharField(max_length=100, verbose_name='Ülke Adı')),
                ('tournament_name', models.CharField(max_length=100, verbose_name='Turnuva Adı')),
                ('season_name', models.CharField(max_length=100, verbose_name='Sezon Adı')),
                ('season_year', models.CharField(max_length=10, verbose_name='Sezon Yılı')),
                ('hasGlobalHighlights', models.BooleanField(default=False, verbose_name='Global Öne Çıkanlar Var mı?')),
                ('hasEventPlayerStatistics', models.BooleanField(default=False, verbose_name='Oyuncu İstatistikleri Var mı?')),
                ('hasEventPlayerHeatMap', models.BooleanField(default=False, verbose_name='Oyuncu Isı Haritası Var mı?')),
            ],
        ),
    ]
