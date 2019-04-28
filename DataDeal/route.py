from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse

# Create your views here.


def GetTest(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)


def GetTestasd(request):
    return JsonResponse({'b': '123'})


def Show(request):
    return render(request, 'First.html')

