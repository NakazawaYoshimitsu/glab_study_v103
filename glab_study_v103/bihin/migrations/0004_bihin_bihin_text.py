# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-29 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bihin', '0003_userinfo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bihin',
            name='bihin_text',
            field=models.TextField(null=True, verbose_name='備考'),
        ),
    ]
