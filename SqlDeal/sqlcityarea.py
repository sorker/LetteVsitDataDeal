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

from DataDealApp.models import CityArea


def insert_city_area(city, city_area):
    CityArea.objects.get_or_create(city=city, city_area=city_area)


def select_city_area():
    all_city = CityArea.objects.all().values_list()
    return all_city


if __name__ == '__main__':
    print(select_city_area())
