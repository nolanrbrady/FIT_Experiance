# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 22:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0007_auto_20170112_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.TextField(blank=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
