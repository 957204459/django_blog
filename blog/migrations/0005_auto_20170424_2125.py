# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='headimage',
            field=models.ImageField(blank=None, default='s', upload_to='head_pic/'),
            preserve_default=False,
        ),
    ]
