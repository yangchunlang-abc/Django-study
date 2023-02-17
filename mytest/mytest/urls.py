"""mytest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 报错不用管
from app01 import views
from django.contrib import admin
from django.urls import path
# 配置路径 网站路径对应执行的函数
# 配置网站路径 后面有对应函数
# 对应的函数返回一个页面
urlpatterns = [
    path('index/', views.index)
]
# url和函数的对应关系
