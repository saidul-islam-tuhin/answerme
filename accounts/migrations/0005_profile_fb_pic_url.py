# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-01 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_profile_read_notifications_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fb_pic_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]