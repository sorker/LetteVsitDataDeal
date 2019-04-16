# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/15 16:04
 @desc    : complaintrawdata数据库操作
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataDeal.settings')
django.setup()

from DataDealApp.models import ComplaintRawData


def sql_insert_complaintrawdata(title, content, reflecting_time, reply_unit, reply_time, reply_opinion, city, area):
    ComplaintRawData.objects.get_or_create(title=title, content=content, reflecting_time=reflecting_time,
                                           reply_unit=reply_unit, reply_time=reply_time, reply_opinion=reply_opinion,
                                           city=city, city_area=area)
