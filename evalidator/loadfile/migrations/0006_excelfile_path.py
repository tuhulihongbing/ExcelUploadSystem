# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-20 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loadfile', '0005_auto_20170220_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='excelfile',
            name='path',
            field=models.FileField(blank=True, null=True, upload_to='./upload/'),
        ),
    ]