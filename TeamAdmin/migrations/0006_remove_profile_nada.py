# Generated by Django 2.2 on 2020-11-02 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TeamAdmin', '0005_auto_20201015_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='nada',
        ),
    ]