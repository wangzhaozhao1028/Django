#coding=utf-8
from django.contrib import admin
from models import Article

# Register your models here.


#改变注册方式 : 显示字段
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')
    list_filter = ('pub_time',)

# 配置应用
admin.site.register(Article,ArticleAdmin)