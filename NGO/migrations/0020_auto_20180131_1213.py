# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0019_auto_20180131_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='image',
            field=models.ImageField(upload_to='children/'),
        ),
    ]
