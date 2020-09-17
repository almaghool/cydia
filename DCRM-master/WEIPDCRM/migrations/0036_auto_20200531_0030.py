# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-30 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0035_auto_20200301_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='show_advertisement',
            field=models.BooleanField(default=False, help_text='Check it to display advertisement.', verbose_name='Show Advertisement'),
        ),
        migrations.AddField(
            model_name='setting',
            name='show_notice',
            field=models.BooleanField(default=False, help_text='Check it to display notice.', verbose_name='Show Notice'),
        ),
    ]
