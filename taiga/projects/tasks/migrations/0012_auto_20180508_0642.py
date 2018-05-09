# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-08 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20160928_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='estimated_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='estimated_end'),
        ),
        migrations.AddField(
            model_name='task',
            name='estimated_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='estimated_start'),
        ),
    ]
