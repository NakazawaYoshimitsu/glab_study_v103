# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-22 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bihin', '0002_auto_20170121_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='status',
            field=models.IntegerField(choices=[(0, '保管中'), (1, '貸出中'), (2, '廃棄')], default=0, verbose_name='状態'),
            preserve_default=False,
        ),
    ]
