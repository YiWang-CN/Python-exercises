#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#coding:utf-8
from django.shortcuts import render,HttpResponse,redirect
from models import Message,UserInfo
import json

# Create your views here.

def index(request):
    if request.method=="POST":
        username = request.POST.get("username")
        content = request.POST.get("content")
        users = UserInfo.objects.filter(username=username)
        if (not content) or (not username):
            return redirect("/index/")
        if not users:
            user = UserInfo.objects.create(username=username)
        else:
            user = users[0]
        message_obj = Message.objects.create(user=user,content=content)
        message={"create_time":message_obj.create_time.strftime("%Y-%m-%d %H:%M:%S")} #auto_now_add时间必须格式化后才能用json处理
        #print message
        return HttpResponse(json.dumps(message))
    messages = Message.objects.all().order_by("-nid")[0:10]  #逆序排列，使最新的留言的排在最前面
    return render(request,"index.html",locals())

