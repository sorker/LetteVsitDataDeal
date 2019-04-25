# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/24 15:08
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
from SqlDeal.sqlcomplaintrawdata import sql_insert_id_classification, sql_select_id_title

file = open('../data/deal/class.txt', 'w+', encoding='utf-8')
categorys = []

for id, title in sql_select_id_title():
    if '<' in title:
        classification = title.split('<')[1].split('>')[0]
        sql_insert_id_classification(id=id, classification=classification)
        if classification not in categorys:
            categorys.append(classification)
    else:
        continue

for category in categorys:
    file.writelines(category + '\n')
