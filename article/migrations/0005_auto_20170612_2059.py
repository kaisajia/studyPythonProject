# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-12 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(choices=[(0, '正常'), (-1, '无效'), (10, '精华')], default=0, verbose_name='状态'),
        ),
    ]