# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-23 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170423_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='owner',
        ),
    ]