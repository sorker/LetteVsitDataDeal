from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

# Create your views here.

def GetTest(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)


def GetTestasd(request):
    return redirect('/?msg=未设置域名和服务器内容')