# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 18:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0005_auto_20160516_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editshtml',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 18, 55, 43, 251341)),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 18, 55, 43, 250758)),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 17)),
        ),
    ]
