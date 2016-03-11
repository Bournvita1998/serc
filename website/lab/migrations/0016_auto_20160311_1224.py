# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0015_auto_20160311_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publication_author', to='lab.ShortNames'),
        ),
    ]
