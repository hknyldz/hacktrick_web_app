# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0026_auto_20170309_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertraining',
            name='user_status',
            field=models.BooleanField(default=False, verbose_name='Katılımcı durumu'),
        ),
    ]