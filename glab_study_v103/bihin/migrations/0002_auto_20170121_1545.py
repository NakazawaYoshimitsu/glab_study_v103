# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-21 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bihin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='display',
            name='id',
        ),
        migrations.RemoveField(
            model_name='keybord',
            name='id',
        ),
        migrations.RemoveField(
            model_name='lease',
            name='id',
        ),
        migrations.RemoveField(
            model_name='mouse',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='display',
            name='bihin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='display', serialize=False, to='bihin.Bihin'),
        ),
        migrations.AlterField(
            model_name='keybord',
            name='bihin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='keyboard', serialize=False, to='bihin.Bihin'),
        ),
        migrations.AlterField(
            model_name='lease',
            name='bihin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='lease', serialize=False, to='bihin.Bihin'),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='bihin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='mouse', serialize=False, to='bihin.Bihin'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='bihin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='userinfo', serialize=False, to='bihin.Bihin'),
        ),
    ]
