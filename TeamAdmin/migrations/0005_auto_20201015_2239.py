# Generated by Django 2.2 on 2020-10-15 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamAdmin', '0004_auto_20201015_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='entrenamiento',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Entrenamiento'),
        ),
    ]