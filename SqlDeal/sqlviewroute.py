# -*- coding:utf-8 -*-
"""
 @time    : 2019/5/1 10:15
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataDeal.settings')
django.setup()

from DataDealApp.models import DepartmentWordWeight, CityAreaDepartment, ClassificationWeight, \
    DepartmentClassificationForUser


def classification_number_out():
    classification_number = ClassificationWeight.objects.all().values('classification', 'number')
    return classification_number


def department_frequency_out():
    department_frequency = CityAreaDepartment.objects.all().values('department', 'frequency')
    return department_frequency


def department_classification_foruser(city, area, department, context, classification):
    if DepartmentClassificationForUser.objects.get(context=context):
        department_classification = DepartmentClassificationForUser.objects.all().values('classification', 'department')
        department_classification['message'] = '数据已存在'
        return department_classification
    else:
        department_classification = DepartmentClassificationForUser.objects.get_or_create(city=city, city_area=area,
                                                                                          department=department,
                                                                                          context=context,
                                                                                          classification=classification)
        department_classification['message'] = '提交成功'
        return department_classification


if __name__ in '__mian__':
    print(department_frequency_out())
