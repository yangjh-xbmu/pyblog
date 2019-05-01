from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='博客分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = "博客分类"


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name='标签')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '内容标签'
        verbose_name_plural = '内容标签'


class Entry(models.Model):
    title = models.CharField(max_length=256, verbose_name='条目标题')
    author = models.ForeignKey(User, verbose_name='条目作者', on_delete=models.CASCADE, )
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='条目添加日期')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='条目修改时间')
    abstract = models.TextField(max_length=256, verbose_name='内容摘要', blank=True, null=True)
    body = models.TextField(verbose_name='条目正文')
    img = models.ImageField(upload_to='blog-images', null=True, blank=True, verbose_name='条目配图')
    visited = models.PositiveIntegerField(default=0, verbose_name='条目访问量')
    category = models.ManyToManyField('Category', verbose_name='条目类别')
    tag = models.ManyToManyField('Tag', verbose_name='条目标签')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = '条目'
        verbose_name_plural = '条目'
