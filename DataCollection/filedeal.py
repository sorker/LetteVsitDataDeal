# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/16 13:19
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
from SqlDeal.sqlcityarea import insert_city_area, insert_city_area_department, select_departmentwordwight_id
from SqlDeal.sqlcomplaintrawdata import sql_select_city_area_department, sql_select_classification
from config import DEAL_DIR, DATA_DIR
import os


# 浙江省城市、区整理
def city_area():
    """
    浙江省城市、区整理
    :return:
    """
    print('开始浙江省城市、区整理')
    filename = os.path.join(DATA_DIR, 'city_area.txt')
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

    print('浙江省城市、区整理完成')


# 浙江省城市、区下的行政部门整理 先生成部门权重表
def city_area_department():
    """
    浙江省城市、区下的行政部门整理
    :return:
    """
    print('开始运行市、区下的行政部门整理 先生成部门权重表')
    city_area_department = sql_select_city_area_department()
    department_frequency = {}
    for city, area, department in city_area_department:
        seg = city + ',' + area + ',' + department
        if department_frequency.__contains__(seg):
            department_frequency[seg] += 1
        else:
            department_frequency[seg] = 1
    for city_area_department_str, frequency in department_frequency.items():
        city, area, department = city_area_department_str.split(',')
        try:
            insert_city_area_department(city, area, department, frequency, select_departmentwordwight_id(department))
        except Exception as e:
            print(e)
            print(department)
            continue
    print('数据整理完成')


# 停用词表
def stopkey():  # 停用词
    file1 = open(os.path.join(DEAL_DIR, '中文停用词表.txt'), 'r', encoding='utf-8')
    file2 = open(os.path.join(DEAL_DIR, '哈工大停用词表.txt'), 'r', encoding='utf-8')
    file3 = open(os.path.join(DEAL_DIR, '四川大学机器智能实验室停用词库.txt'), 'r', encoding='utf-8')
    file5 = open(os.path.join(DEAL_DIR, '1208个停用词.txt'), 'r', encoding='utf-8')
    file4 = open(os.path.join(DATA_DIR, '停用词表.txt'), 'w+', encoding='utf-8')
    words1 = file1.readlines()
    words2 = file2.readlines()
    words3 = file3.readlines()
    words5 = file5.readlines()
    words4 = []
    for word in words1:
        if word not in words2 and word not in words3:
            words4.append(word)
    for word in words2:
        if word not in words4:
            words4.append(word)
    for word in words3:
        if word not in words4:
            words4.append(word)
    for word in words5:
        if word not in words4:
            words4.append(word)
    for word in words4:
        file4.writelines(word)
    # for word in words:
    #     print(word)


# 类别文件
def classification_write():
    file = open('../data/类别.txt', 'w+', encoding='utf-8')
    for classification in sql_select_classification():
        file.writelines(classification + ',')


if __name__ in "__main__":
    city_area()
    # classification_write()
    # city_area_department()
    # stopkey()
    # a = ['1', '2']
    # c, d = a
    # print(c, d)
