# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitr', '0009_auto_20171115_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='day',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='from_hour',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='to_hour',
        ),
        migrations.AddField(
            model_name='schedule',
            name='end',
            field=models.DateTimeField(default='2017-11-15 17:50:03.616271'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='start',
            field=models.DateTimeField(default='2017-11-15 17:50:03.616271'),
            preserve_default=False,
        ),
    ]
