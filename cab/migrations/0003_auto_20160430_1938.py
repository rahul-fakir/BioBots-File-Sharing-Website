# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0002_auto_20160428_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='extuser',
            name='forgotKey',
            field=models.CharField(default=3, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='extuser',
            name='email',
            field=models.EmailField(db_index=True, max_length=255, unique=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='extuser',
            name='firstname',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='extuser',
            name='lastname',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name=''),
        ),
    ]
