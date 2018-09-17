#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0.0'
'''
@Time    : 2018/9/16 0016 18:09
@Author  : Van Huang
@Email   : huangvan0808@gmail.com
@File    : urls.py
@Software: PyCharm
@details : 为应用程序users定义URL模式

'''

from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]

