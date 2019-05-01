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
from DataCollection.calculationdeal import tuple_to_dict


def classification_number_out():
    classification_number = ClassificationWeight.objects.all().values_list('classification', 'number')
    return tuple_to_dict(classification_number)


def department_frequency_out():
    department_frequency = CityAreaDepartment.objects.all().values_list('department', 'frequency')
    return tuple_to_dict(department_frequency)


def city_area_number():
    area_number = CityAreaDepartment.objects.all().annotate(count=Count('city_area'))


def department_classification_foruser(city, area, department, context, classification):
    try:
        DepartmentClassificationForUser.objects.get(context=context)
        department_classification = \
        DepartmentClassificationForUser.objects.all().values('classification', 'department')[0]
        department_classification['message'] = '数据已存在'
        return department_classification
    except:
        department_classification = {}
        DepartmentClassificationForUser.objects.get_or_create(city=city, city_area=area, department=department,
                                                              context=context,
                                                              classification=classification)
        department_classification['message'] = '提交成功'
        return department_classification


if __name__ in '__main__':
    print(classification_number_out())
    # print(department_classification_foruser('杭州', '上城区', '杭州市上城区小营街道',
    #                                         '我是下华光巷70号4单元502的住户，屋顶在多年前平改坡，漏水问题好了很多。最近我发现有人再我屋顶种蔬菜，这样屋顶被堆放杂物和频繁的踩踏，容易破坏屋顶。现向管理部门反映情况，麻烦管理部门能帮忙清理掉这些杂物。',
    #                                         '城管执法'))
