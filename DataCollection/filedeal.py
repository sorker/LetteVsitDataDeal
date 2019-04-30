# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/16 13:19
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
from SqlDeal.sqlcityarea import insert_city_area, insert_city_area_department
from SqlDeal.sqlcomplaintrawdata import sql_select_city_area_department, sql_select_classification


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

    print('插入完成')


def city_area_department():
    """
    浙江省城市、区下的行政部门整理
    :return:
    """
    city_area_department = sql_select_city_area_department()
    n = 0
    for city, area, department in city_area_department:
        insert_city_area_department(city, area, department)


def stopkey():
    file1 = open('../data/deal/中文停用词表.txt', 'r', encoding='utf-8')
    file2 = open('../data/deal/哈工大停用词表.txt', 'r', encoding='utf-8')
    file3 = open('../data/deal/四川大学机器智能实验室停用词库.txt', 'r', encoding='utf-8')
    file5 = open('../data/deal/1208个停用词.txt', 'r', encoding='utf-8')
    file4 = open('../data/停用词表.txt', 'w+', encoding='utf-8')
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


def classification_write():
    file = open('../data/类别.txt', 'w+', encoding='utf-8')
    for classification in sql_select_classification():
        file.writelines(classification + ',')


if __name__ in "__main__":
    # city_area()
    classification_write()
