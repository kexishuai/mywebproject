# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sex', models.BooleanField(default=True)),
                ('icon', models.FileField(blank=True, null=True, upload_to='')),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
