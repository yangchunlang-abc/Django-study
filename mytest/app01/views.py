from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# 写执行的函数
def index(request):
    #  去app目录下templates寻找文件
    return render(request, 'index.html')
