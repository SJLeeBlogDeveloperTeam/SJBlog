# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50, blank=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyBlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100, blank=True)),
                ('intro', models.TextField(max_length=500, blank=True)),
                ('content', models.TextField(max_length=99999)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('website', models.URLField(blank=True)),
                ('count_hit', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200, verbose_name='\u540d\u79f0')),
                ('count_post', models.IntegerField(default=0, verbose_name='\u6587\u7ae0\u6570', editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='myblog',
            name='tags',
            field=models.ManyToManyField(to='Blog.Tag', verbose_name='\u6807\u7b7e', blank=True),
        ),
    ]
