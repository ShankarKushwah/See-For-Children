# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0015_remove_children_photos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NGO.Children')),
            ],
        ),
    ]