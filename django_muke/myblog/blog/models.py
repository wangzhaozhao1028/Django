#coding=utf-8
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    # admin管理页面设置显示标题页
    def __unicode__(self):
        return self.title