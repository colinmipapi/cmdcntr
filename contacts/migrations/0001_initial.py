# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('phone', models.CharField(blank=True, max_length=500, null=True)),
                ('source', models.CharField(blank=True, max_length=500, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]