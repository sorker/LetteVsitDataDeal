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


def sql_select_title():
    title = ComplaintRawData.objects.values_list('title')
    return title


def sql_select_department_content():
    content_department = ComplaintRawData.objects.filter(read_times=True).values_list('content', 'reply_unit')
    ComplaintRawData.objects.filter(read_times=True).update(read_times=False)
    return content_department


if __name__ == '__main__':
    print(sql_select_department_content())
