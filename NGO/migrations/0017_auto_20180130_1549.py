# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0016_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(upload_to='photo_gallery/'),
        ),
    ]