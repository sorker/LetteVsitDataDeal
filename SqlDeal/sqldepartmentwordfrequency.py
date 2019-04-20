# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/20 18:45
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataDeal.settings')
django.setup()

from DataDealApp.models import DepartmentWordFrequency


def insert_department_word_frequency(department, word, frequency):
    DepartmentWordFrequency.objects.get_or_create(department, word, frequency)
