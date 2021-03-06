# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitr', '0002_auto_20171113_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitr.Applicant')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitr.Position')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitr.Recruiter')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitr.Schedule')),
            ],
        ),
    ]
