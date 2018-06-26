# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20171007_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]