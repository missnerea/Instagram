# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gramygram', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]