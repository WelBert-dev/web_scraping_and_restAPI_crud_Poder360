# Generated by Django 4.2.9 on 2024-01-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trigger_web_scraping_dou_api', '0006_alter_detailsinglejournalofdou_assina_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsinglejournalofdou',
            name='versao_certificada',
            field=models.URLField(unique=False),
        ),
    ]