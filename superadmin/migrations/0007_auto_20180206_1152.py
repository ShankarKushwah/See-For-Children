# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-06 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0006_auto_20180206_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
