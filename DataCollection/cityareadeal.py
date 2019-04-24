# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/16 13:19
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
from SqlDeal.sqlcityarea import insert_city_area, insert_city_area_department
from SqlDeal.sqlcomplaintrawdata import sql_select_city_area_department


def city_area():
    """
    浙江省城市、区整理
    :return:
    """
    filename = '../data/city_area.txt'
    file = open(filename, mode='r')
    text = file.readlines()
    # print(text)
    city_area = []
    city = ''
    for txt in text:
        if txt == '\n':
            continue
        elif '\t\n' in txt:
            city = txt.expandtabs(tabsize=8).split()[0]
            continue
        else:
            city_area.append([city, str(txt).splitlines()[0]])

    for city, area in city_area:
        insert_city_area(city, area)

    print(city, ',', area, '插入完成')


def city_area_department():
    """
    浙江省城市、区下的行政部门整理
    :return:
    """
    city_area_department = sql_select_city_area_department()
    for city, area, department in city_area_department:
        insert_city_area_department(city, area, department)


if __name__ in "__main__":
    city_area_department()
