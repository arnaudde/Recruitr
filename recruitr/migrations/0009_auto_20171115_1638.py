# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitr', '0008_auto_20171114_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruitr.Schedule'),
        ),
    ]