# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-28 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityNum', models.IntegerField(blank=True, null=True)),
                ('city_name', models.CharField(max_length=50)),
                ('city_state', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
