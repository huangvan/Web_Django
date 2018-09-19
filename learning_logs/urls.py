#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0.0'
'''
@Time    : 2018/9/15 0015 16:39
@Author  : Van Huang
@Email   : huangvan0808@gmail.com
@File    : urls.py.py
@Software: PyCharm
@details : 定义learning_logs的URL模式

'''
from django.urls import path, include
from . import views

app_name = 'learning_logs'


urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    path(r'^del_entry/(?P<entry_id>\d+)/$', views.del_entry, name='del_entry'),
    path(r'^edit_topic/(?P<topic_id>\d+)/$', views.edit_topic, name='edit_topic'),
    path(r'^del_topic/(?P<topic_id>\d+)/$', views.del_topic, name='del_topic'),
]








