# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 19:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fit.Dimension')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fit.SubCategory')),
            ],
        ),
    ]
