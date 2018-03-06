# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-06 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0051_auto_20180306_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='training_finish_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Eğitim kayıt bitiş tarihi'),
            preserve_default=False,
        ),
    ]