# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-03-07 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20190307_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='scheduled_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]