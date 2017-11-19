# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitr', '0005_remove_applicant_recruiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='dynamism',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='experience',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='interest',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
    ]