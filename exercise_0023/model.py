#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserInfo(AbstractUser):

    def __str__(self):
        return self.username
    class Meta:
        verbose_name="用户"
        verbose_name_plural=verbose_name

class Message(models.Model):
    nid = models.AutoField(primary_key=True)
    content=models.CharField(max_length=512)
    user = models.ForeignKey(to='UserInfo')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nid

    class Meta:
        verbose_name="留言内容"
        verbose_name_plural=verbose_name
