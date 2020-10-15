# Generated by Django 2.2 on 2020-10-15 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(default='', max_length=20)),
                ('contraseña', models.CharField(default='', max_length=20)),
                ('nombre', models.CharField(default='', max_length=20)),
                ('apellido', models.CharField(default='', max_length=20)),
                ('dni', models.CharField(default='', max_length=20)),
                ('telefono', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Entrenamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(default='', max_length=20)),
                ('contraseña', models.CharField(default='', max_length=20)),
                ('nombre', models.CharField(default='', max_length=20)),
                ('apellido', models.CharField(default='', max_length=20)),
                ('dni', models.CharField(default='', max_length=20)),
                ('telefono', models.CharField(default='', max_length=20)),
                ('deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Deporte')),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrincante', models.CharField(default='', max_length=20)),
                ('puntoContrincante', models.IntegerField()),
                ('puntoEquipo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrenamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Entrenamiento')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Partido')),
            ],
        ),
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('minuto', models.CharField(default='', max_length=20)),
                ('tiempo', models.CharField(default='', max_length=20)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Jugador')),
            ],
        ),
        migrations.AddField(
            model_name='partido',
            name='punto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Punto'),
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
                ('fecha', models.DateField()),
                ('horaInicio', models.TimeField()),
                ('horaFin', models.TimeField()),
                ('asistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Jugador')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Deporte')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
                ('deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Deporte')),
                ('entrenadores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Entrenador')),
                ('jugadores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Jugador')),
            ],
        ),
        migrations.AddField(
            model_name='deporte',
            name='posicion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamAdmin.Posicion'),
        ),
    ]
