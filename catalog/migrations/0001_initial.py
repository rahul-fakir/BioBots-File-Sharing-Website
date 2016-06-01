# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 18:21
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('dowloads', models.IntegerField(default=0)),
                ('size', models.FloatField(default=0.0)),
                ('date_published', models.DateTimeField(default=datetime.datetime(2016, 4, 27, 18, 21, 38, 799065))),
                ('f', models.FileField(blank=True, null=True, upload_to='media/files/')),
            ],
        ),
        migrations.CreateModel(
            name='fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('path', models.FileField(blank=True, null=True, upload_to='media/fotos/')),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_published', models.DateTimeField(default=datetime.datetime(2016, 4, 27, 18, 21, 38, 797329))),
                ('foto', models.TextField()),
                ('information', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('tags', models.TextField()),
                ('main_foto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.fotos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='foto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.fotos'),
        ),
        migrations.AddField(
            model_name='file',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.item'),
        ),
    ]
