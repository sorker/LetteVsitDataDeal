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

from DataDealApp.models import ComplaintRawData, ClassificationWeight


def sql_insert_complaintrawdata(title, content, reflecting_time, reply_unit, reply_time, reply_opinion, city, area):
    ComplaintRawData.objects.get_or_create(title=title, content=content, reflecting_time=reflecting_time,
                                           reply_unit=reply_unit, reply_time=reply_time, reply_opinion=reply_opinion,
                                           city=city, city_area=area)


def sql_select_title():
    title = ComplaintRawData.objects.filter(read_times=True).values_list('title')
    return title


def sql_select_classification_context():
    sql_content_departments = ComplaintRawData.objects.filter(read_times=True).exclude(
        contextwordfrequency__classification=None).select_related('contextwordfrequency')
    content_departments = []
    for content_department in sql_content_departments:
        content_departments.append([content_department.contextwordfrequency.classification, content_department.content])
    return content_departments



def sql_select_department_content():
    content_department = ComplaintRawData.objects.filter(read_times=True).values_list('content', 'reply_unit')
    # ComplaintRawData.objects.filter(read_times=True).update(read_times=False)
    return content_department


def sql_select_id_department_content():
    content_department = ComplaintRawData.objects.filter(read_times=True).order_by(
        'reply_unit').values_list('id', 'content', 'reply_unit')
    # print(len(content_department))
    # ComplaintRawData.objects.filter(read_times=True).update(read_times=False)
    return content_department


def sql_select_id_title_department_content():
    id_title_department_content = ComplaintRawData.objects.filter(read_times=True).values_list('id', 'title', 'content',
                                                                                               'reply_unit')
    # print(len(content_department))
    # ComplaintRawData.objects.filter(read_times=True).update(read_times=False)
    return id_title_department_content


def sql_select_city_area_department():
    city_area_department = ComplaintRawData.objects.filter(read_times=True).values_list('city', 'city_area',
                                                                                        'reply_unit')
    return city_area_department


def sql_insert_classification_weight(classification, number, words, weight):
    ClassificationWeight.objects.get_or_create(classification=classification, number=number, words=words, weight=weight)


def sql_select_classification_weight():
    sel_data = ClassificationWeight.objects.all().values('classification', 'words', 'weight')
    classification_words_weights = sql_to_dict(sel_data, 'classification', 'words', 'weight')
    return classification_words_weights


def sql_select_classification():
    classifications = []
    for classification in ClassificationWeight.objects.values('classification'):
        classifications.append(classification['classification'])
    return classifications


def sql_to_dict(sql_data, *args):  # 把数据库中的分词权重变成可遍历的字典
    """
    :param sql_data:
    :param args: 类别， 分词， 权重的数据库值
    :return:
    """
    words_weights = {}
    for classification_words_weight in sql_data:
        words = classification_words_weight[args[1]].split(',')
        words.pop()
        # print(words)
        weights = classification_words_weight[args[2]].split(',')
        weights.pop()
        word_weigtht = {}
        # for word, weight in words, weights:
        #     word_weigtht[word] = weight
        for k, word in enumerate(words):
            if word is not '':
                word_weigtht[word] = weights[k]
        words_weights[classification_words_weight[args[0]]] = word_weigtht
    return words_weights


if __name__ == '__main__':
    # print(sql_select_classification_context()[6])
    # print(sql_select_classification_context()[7])
    # print(sql_select_classification_context()[8])
    # print(sql_select_classification_context()[9])
    for a in sql_select_id_department_content():
        print(a)
    # ComplaintRawData.objects.filter(read_times=False).update(read_times=True)
