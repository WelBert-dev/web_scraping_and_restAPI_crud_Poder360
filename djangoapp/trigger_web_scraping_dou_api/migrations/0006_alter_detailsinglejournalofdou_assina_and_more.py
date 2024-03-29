# Generated by Django 4.2.9 on 2024-01-18 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trigger_web_scraping_dou_api', '0005_detailsinglejournalofdou'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsinglejournalofdou',
            name='assina',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='detailsinglejournalofdou',
            name='cargo',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='detailsinglejournalofdou',
            name='edicao_dou_data',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='detailsinglejournalofdou',
            name='orgao_dou_data',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='detailsinglejournalofdou',
            name='paragrafos',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='detailsinglejournalofdou',
            name='publicado_dou_data',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='detailsinglejournalofdou',
            name='secao_dou_data',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='detailsinglejournalofdou',
            name='title',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='artType',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='editionNumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='hierarchyLevelSize',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='hierarchyList',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='hierarchyStr',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='numberPage',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='pubDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='pubName',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='pubOrder',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='subTitulo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='titulo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='journaljsonarrayofdou',
            name='urlTitle',
            field=models.CharField(),
        ),
    ]
