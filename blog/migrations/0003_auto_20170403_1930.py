# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-03 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200, verbose_name='\u793e\u4ea4')),
                ('link', models.URLField(max_length=512, verbose_name='\u94fe\u63a5')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=200, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
                ('detail', models.CharField(max_length=512, verbose_name='\u8be6\u60c5')),
            ],
        ),
        migrations.CreateModel(
            name='ContributedProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u9879\u76ee')),
                ('link', models.URLField(max_length=512, verbose_name='\u94fe\u63a5')),
            ],
        ),
        migrations.CreateModel(
            name='OpenSourceProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u9879\u76ee')),
                ('link', models.URLField(max_length=512, verbose_name='\u94fe\u63a5')),
            ],
        ),
        migrations.AlterModelOptions(
            name='resume',
            options={'ordering': ['-id']},
        ),
    ]
