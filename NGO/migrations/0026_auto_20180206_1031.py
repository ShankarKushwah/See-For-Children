# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-06 05:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0025_auto_20180202_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='ngo',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
