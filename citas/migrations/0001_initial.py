# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('nombre_legal', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('fono', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=100)),
                ('web', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id_rut', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('nombres', models.CharField(max_length=100)),
                ('paterno', models.CharField(max_length=100)),
                ('materno', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=100)),
                ('fono', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('centro', models.ForeignKey(to='citas.Centro')),
                ('especialidad', models.ForeignKey(to='citas.Especialidad')),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_rut', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('nombres', models.CharField(max_length=100)),
                ('paterno', models.CharField(max_length=100)),
                ('materno', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=100)),
                ('celular', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Prevision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Prevision',
                'verbose_name_plural': 'Previsiones',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_reserva', models.DateField()),
                ('hora_reserva', models.TimeField()),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(max_length=50)),
                ('confirmado', models.BooleanField()),
                ('idMedico', models.ForeignKey(to='citas.Medico')),
                ('idPaciente', models.ForeignKey(to='citas.Paciente')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.AddField(
            model_name='paciente',
            name='prevision',
            field=models.ForeignKey(to='citas.Prevision'),
        ),
    ]
