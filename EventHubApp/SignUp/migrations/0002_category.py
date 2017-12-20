# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-28 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignUp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('category_url', models.CharField(max_length=50)),
            ],
        ),
    ]