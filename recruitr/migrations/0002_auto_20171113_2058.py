# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='position',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='skills',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
        migrations.AddField(
            model_name='position',
            name='skill',
            field=models.ManyToManyField(to='recruitr.Skill'),
        ),
        migrations.AddField(
            model_name='recruiter',
            name='skill',
            field=models.ManyToManyField(to='recruitr.Skill'),
        ),
    ]
