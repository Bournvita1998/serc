# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0027_auto_20160404_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawResourceSkeleton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='static/images/resource')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ResourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('display_text', models.CharField(max_length=40)),
                ('display_type', models.IntegerField(choices=[(1, 'Type = Link'), (2, 'Type = Project')])),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='rawresourceskeleton',
            name='list_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.ResourceType'),
        ),
    ]
