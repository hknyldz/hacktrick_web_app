# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-06 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0054_remove_setting_participant_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertraining',
            name='user_status',
            field=models.BooleanField(default=True, verbose_name='Katılımcı durumu'),
        ),
    ]