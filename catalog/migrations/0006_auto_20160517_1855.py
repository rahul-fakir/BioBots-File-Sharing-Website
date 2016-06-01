# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 18:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20160516_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libraries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/libraryimage/')),
            ],
        ),
        migrations.AlterField(
            model_name='file',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 18, 55, 43, 240671)),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 18, 55, 43, 237388)),
        ),
    ]
