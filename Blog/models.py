# coding:utf-8
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)  # 博客题目
    category = models.CharField(max_length=50, blank=True)  # 博客标签
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = models.TextField(blank=True, null=True)  # 博客文章正文

    def __unicode__(self):
        return self.title


class Meta:  # 按时间降序
        ordering = ['-date_time']


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=u'名称')
    count_post = models.IntegerField(default=0, editable=False, verbose_name=u'文章数')

    def __unicode__(self):
        return self.name


class MyBlog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    intro = models.TextField(max_length=500, blank=True)
    content = models.TextField(max_length=99999)
    pub_date = models.DateTimeField(auto_now_add=True)
    website = models.URLField(blank=True)
    count_hit = models.IntegerField(default=0, editable=False, verbose_name=u'点击数')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')

    def __unicode__(self):
        return self.title

