# Generated by Django 2.2 on 2020-11-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamAdmin', '0003_auto_20201126_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descripcion',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='evento',
            name='puntoEquipo',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
