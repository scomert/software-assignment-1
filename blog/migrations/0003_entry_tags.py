# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_remove_tag_entry'),
        ('blog', '0002_entry_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
    ]
