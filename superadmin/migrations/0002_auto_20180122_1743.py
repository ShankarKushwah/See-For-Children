# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='child_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='NGO.Children'),
        ),
    ]