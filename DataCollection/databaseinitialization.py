# -*- coding:utf-8 -*-
"""
 @time    : 2019/5/1 9:57
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
from DataCollection.registration import registeration
from DataCollection.rawdatadeal import all_classification_words_weight, all_department_weight, all_classification_weight
from DataCollection.filedeal import city_area_department
from SqlDeal.sqldeletedata import sql_delete_data
from time import sleep

def database_initialization():
    sql_delete_data()
    registeration.next_area()
    all_classification_words_weight()
    all_department_weight()
    all_classification_weight()
    city_area_department()


if __name__ in "__main__":
    while True:
        database_initialization()
        sleep(3600)

