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
    department_classification = {}
    try:
        city, area, context = request.GET['city'], request.GET['area'], request.GET['context']
        try:
            DepartmentClassificationForUser.objects.check(context=context)
            department_classification = \
            DepartmentClassificationForUser.objects.filter(context=context).values('classification', 'department')[0]
            department_classification['message'] = '数据已存在'
            return JsonResponse(department_classification)
        except Exception as e:
            if city or area or context:
                classification_number = recommend_five(class_sort(context))
                department_frequency = recommend_five(department_sort(context, city, area))
                department_classification['classification'] = classification_number
                department_classification['department'] = department_frequency
                department_classification['message'] = '处理完成'
            # print(department_classification)
    except Exception as e:
        department_classification['message'] = '请输入城市、地点、内容'
    return JsonResponse(department_classification)


def department_frequency_port(request):
    return JsonResponse(department_frequency_out())


def classification_number_port(request):
    return JsonResponse(classification_number_out())


def sort_out(request):
    department_classification = {}
    try:
        city, area, department, context, classification = request.GET['city'], request.GET['area'], request.GET[
            'department'], request.GET['context'], request.GET['classification']
        department_classification = department_classification_foruser(city, area, department, context, classification)
    except:
        department_classification['message'] = '请输入城市、地点、部门、内容、、类别'
    return JsonResponse(department_classification)


def city_area_count(request):
    return JsonResponse(city_area_number())


if __name__ in '__main__':
    print(recommend_five(class_sort('电视里播放萨鲁的烦恼拉萨的妇女')))
    # print(DepartmentClassificationForUser.objects.filter(id='1').values('classification', 'department')[0])
