# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-19 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPortfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]