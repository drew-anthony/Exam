# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-24 17:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_auto_20180724_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='likes',
            new_name='many',
        ),
    ]
