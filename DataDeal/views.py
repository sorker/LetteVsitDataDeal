# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/27 22:43
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
from SqlDeal.sqlviewroute import classification_number_out, department_frequency_out, department_classification_foruser, DepartmentClassificationForUser
from DataCollection.calculationdeal import recommend_five, department_sort, class_sort, tuple_to_dict
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse


def deparment_class_sort_out(request):
    if DepartmentClassificationForUser.objects.get(context=request.context):
        department_classification = DepartmentClassificationForUser.objects.all().values('classification', 'department')
        department_classification['message'] = '数据已存在'
        return JsonResponse(department_classification)
    else:
        department_classification = {}
        classification_number = tuple_to_dict(recommend_five(class_sort(request.context)))
        department_frequency = tuple_to_dict(recommend_five(department_sort(request.context,
                                                                            request.city, request.area)))
        department_classification['classification'] = classification_number
        department_classification['department'] = department_frequency
        department_classification['message'] = '处理完成'
        return JsonResponse(department_classification)


def department_frequency_port(request):
    return HttpResponse(classification_number_out())


