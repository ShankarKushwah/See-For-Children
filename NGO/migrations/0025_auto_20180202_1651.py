# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-02 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0024_auto_20180202_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
