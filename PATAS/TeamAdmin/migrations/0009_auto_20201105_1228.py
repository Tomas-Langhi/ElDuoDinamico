# Generated by Django 2.2 on 2020-11-05 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TeamAdmin', '0008_auto_20201105_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrenador',
            old_name='useuario',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='jugador',
            old_name='useuario',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='useuario',
            new_name='usuario',
        ),
    ]
