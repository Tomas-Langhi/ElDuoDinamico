# Generated by Django 2.2 on 2020-11-05 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamAdmin', '0007_auto_20201103_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='created_by',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='rol',
        ),
        migrations.AlterField(
            model_name='entrenador',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
