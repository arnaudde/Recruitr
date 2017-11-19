# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitr', '0007_remove_match_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='position',
        ),
        migrations.AddField(
            model_name='applicant',
            name='position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recruitr.Position'),
            preserve_default=False,
        ),
    ]
