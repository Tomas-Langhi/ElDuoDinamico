# Generated by Django 2.2 on 2020-11-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamAdmin', '0005_auto_20201126_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='punto',
            field=models.ManyToManyField(blank=True, null=True, to='TeamAdmin.Punto'),
        ),
    ]
