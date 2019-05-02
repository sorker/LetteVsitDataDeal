# -*- coding:utf-8 -*-
"""
 @time    : 2019/5/1 10:02
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataDeal.settings')
django.setup()

from DataDealApp.models import DepartmentWordWeight, CityAreaDepartment, ClassificationWeight

def sql_delete_data():
    DepartmentWordWeight.objects.all().delete()
    CityAreaDepartment.objects.all().delete()
    ClassificationWeight.objects.all().delete()
