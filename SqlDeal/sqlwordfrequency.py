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

from DataDealApp.models import DepartmentWordFrequency, ContextWordFrequency


def insert_department_word_frequency(department, word, frequency):
    DepartmentWordFrequency.objects.get_or_create(department=department, word=word, frequency=frequency)


def select_all_department_word_frequency():
    return DepartmentWordFrequency.objects.all().order_by('department').values_list('department', 'word', 'frequency')


def insert_id_word_frequency(id, word, frequercy):
    ContextWordFrequency.objects.get_or_create(complaint_raw_data_id=id, word=word, frequency=frequercy)


if __name__ in "__main__":
    print(select_all_department_word_frequency())