# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ziduan(models.Model):
    name = models.CharField(max_length=20)
    length = models.IntegerField()
    Repeatable = models.BooleanField()
    blankable = models.BooleanField()
    islimited = models.BooleanField()
    limitedtablename = models.CharField(max_length=60)
    limitedziduanname = models.CharField(max_length=60)


class User(models.Model):
    headImg = models.FileField(upload_to = './upload/')
    def __unicode__(self):
        return self.headImg

class Folder(models.Model):
    name = models.CharField('文件夹名',max_length=200)
    pub_date = models.DateTimeField('生成日期',auto_now=True)
    parent = models.ForeignKey('self',blank=True,null=True,verbose_name='上级目录')
    # creator = models.CharField(max_length=200)
    # parentid  = models.IntegerField('原路径',default=0)

    def __unicode__(self):
        return self.name

class Excelfile(models.Model):
    name = models.CharField('文件名',max_length=200)
    pub_date = models.DateTimeField('生成日期', auto_now=True)
    folder = models.ForeignKey(Folder)
    path = models.FileField(upload_to='./upload/',null=True, blank=True)
    # creator = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name