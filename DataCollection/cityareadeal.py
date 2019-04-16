# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/16 13:19
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
from SqlDeal.sqlcityarea import insert_city_area


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