# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('cid', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('dob', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=6)),
                ('mobile', models.IntegerField(unique=True)),
                ('grad', models.CharField(max_length=2)),
                ('course', models.CharField(max_length=30)),
                ('college', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=25)),
                ('zip', models.IntegerField()),
                ('mark', models.FloatField(default=b'0')),
                ('rank', models.IntegerField(default=b'0')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cid', models.CharField(max_length=10)),
                ('rid', models.CharField(max_length=10)),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('rid', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=10)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
