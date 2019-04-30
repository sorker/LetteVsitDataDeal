# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/30 14:21
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
import cpca
import jieba
from jieba import analyse
from ConDriver.redisdriver import redisdriver
import operator
from SqlDeal.sqlcomplaintrawdata import sql_select_classification_weight
from config import STOPWORD


def class_sort(context):   # 分类
    classification_words_weights = sql_select_classification_weight()
    segments = word_count_dict(context)
    classifications = open('../data/类别.txt', 'r', encoding='utf-8').readline().split(',')
    classifications.pop()
    classifications_match = {}
    for classification in classifications:
        match = 0
        # print(classification)
        try:
            word_weight = classification_words_weights[classification]
            for word, weight in word_weight.items():  # 如果有则权重相加
                # print(word)
                if segments.__contains__(word):
                    match += float(weight * segments[word])
                else:
                    continue
        except Exception as e:
            print(e)
        classifications_match[classification] = match
    sorted_classifications_match = sorted(classifications_match.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_classifications_match


def word_count_dict(content):  # 分词并计算词频
    segments = {}
    for keyword in jieba.cut(content):
        word = keyword.replace(' ', '')
        if word not in STOPWORD and not keyword.isdigit():
            if word not in segments:
                segments[word] = 1
            else:
                segments[word] += 1
    return segments


def recommend_five(tuple_values):  # 等到匹配度前五
    word_weight = {}
    for word, weight in tuple_values[:5]:
        word_weight[word] = weight
    return word_weight


def department_sort(context, city, area):  # 分部门
    segments = word_count_dict(context)
    fhfd