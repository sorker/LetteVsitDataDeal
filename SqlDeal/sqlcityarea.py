# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/16 13:42
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataDeal.settings')
django.setup()

from DataDealApp.models import CityArea, CityAreaDepartment, DepartmentWordWeight


def insert_city_area(city, city_area):
    CityArea.objects.get_or_create(city=city, city_area=city_area)


def select_city_area():
    print('开始获取城市数据')
    all_city = CityArea.objects.all().values_list()
    # if len(all_city) == 0:
    #     print('城市数据不存在，开始重新整理')
    #     city_area()
    #     print('开始重新获取城市数据')
    #     all_city = CityArea.objects.all().values_list()
    # print('获取城市数据完成')
    return all_city


def insert_city_area_department(city, area, department, frequency, departmentwordwight_id):  # 插入地区部门
    CityAreaDepartment.objects.get_or_create(city=city, city_area=area, department=department, frequency=frequency,
                                             department_word_weight_id=departmentwordwight_id)


def select_departmentwordwight_id(department):  # 找到部门ID
    departmentwordwight_id = DepartmentWordWeight.objects.filter(department=department).values('id')[0]['id']
    return departmentwordwight_id


def select_department_word_weight():
    DepartmentWordWeight.objects.all()


if __name__ == '__main__':
    select_city_area()
