# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0013_auto_20180130_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]