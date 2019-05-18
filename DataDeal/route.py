from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse

# Create your views here.


def Checkchart(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)


def department(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)


def find(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)


def First(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)


def input(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)


def jinlu(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)


def test(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)


def test2(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)


def xuandepartmetn(request):
    context = {'b': 'a'}
    return render(request, 'index.html', context)

