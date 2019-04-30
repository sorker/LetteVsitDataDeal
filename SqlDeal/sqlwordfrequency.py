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

from DataDealApp.models import DepartmentWordWeight, ContextWordFrequency


def insert_department_word_frequency(department, word, weight):
    DepartmentWordWeight.objects.get_or_create(department=department, word=word, weight=weight)


def select_all_department_word_frequency():
    return DepartmentWordWeight.objects.all().order_by('department').values_list('department', 'word', 'weight')


def insert_id_word_frequency(id, classification, word, frequercy):
    ContextWordFrequency.objects.get_or_create(classification=classification, word=word, frequency=frequercy,
                                               complaint_raw_data_id=id)


if __name__ in "__main__":
    print(select_all_department_word_frequency())
