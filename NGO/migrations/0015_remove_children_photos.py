# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0014_auto_20180130_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='children',
            name='photos',
        ),
    ]
