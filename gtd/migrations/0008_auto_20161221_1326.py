# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-21 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtd', '0007_auto_20161221_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleitem',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
    ]
