# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='source',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
