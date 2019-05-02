# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/27 22:43
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
from SqlDeal.sqlviewroute import classification_number_out, department_frequency_out, department_classification_foruser, \
    DepartmentClassificationForUser, city_area_number
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
    return JsonResponse(department_frequency_out())


def classification_number_port(request):
    return JsonResponse(classification_number_out())


def sort_out(request):
    department_classification = department_classification_foruser(request.city, request.area, request.department,
                                                                  request.context, request.classification)
    return JsonResponse(department_classification)


def city_area_count(request):
    return JsonResponse(city_area_number())


# if __name__ in '__main__':
#     print(classification_number_port())