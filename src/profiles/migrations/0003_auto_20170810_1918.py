# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profiles_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profiles',
            new_name='profile',
        ),
    ]
