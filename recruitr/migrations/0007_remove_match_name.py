# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitr', '0006_auto_20171114_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='name',
        ),
    ]
