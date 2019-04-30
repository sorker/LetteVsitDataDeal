# -*- coding:utf-8 -*-
from urllib import request, error, parse
from SqlDeal.sqlcomplaintrawdata import sql_select_title, sql_select_department_content, \
    sql_select_id_department_content, sql_select_id_title_department_content, sql_select_classification_context, \
    sql_insert_classification_weight
from SqlDeal.sqlwordfrequency import insert_department_word_frequency, select_all_department_word_frequency, \
    insert_id_word_frequency
import cpca
import jieba
from jieba import analyse
from ConDriver.redisdriver import redisdriver
from DataCollection.calculationdeal import word_count_dict
from config import STOPWORD


def get_area_in_txt():
    # 获取网页内容
    file = open('../data/deal/titles.txt', mode='w+', encoding='utf-8')
    titles = sql_select_title()
    for title in titles:
        title = title[0]
        # if len(title) > 50:
        #     title = title[0:49]
        file.writelines(title + '\n')
    print('标题数据获取完成')


def get_area_out_txt():
    file = open('../data/deal/titles.txt', mode='r', encoding='utf-8')
    area_out = open('../data/deal/area_out.txt', mode='w+', encoding='utf-8')
    titles = []
    for title in file.readlines():
        titles.append(str(title).splitlines()[0])
    df = cpca.transform(titles, cut=False, lookahead=3)
    area_out.writelines('ID' + '\t' + '省' + '\t' + '市' + '\t' + '区' + '\t' + '地址' + '\n')
    for index, rows in df.iterrows():
        row = str(index) + '\t' + rows['省'] + '\t' + rows['市'] + '\t' + rows['区'] + '\t' + rows['地址'] + '\n'
        area_out.writelines(row)
    print('地点数据获取完成')


def get_context_out_text():
    # file = open('../data/deal/context_percent.txt', mode='w+', encoding='utf-8')
    words = open('../data/停用词表.txt', 'r', encoding='utf-8').readlines()
    contexts = sql_select_department_content()  # 读取数据库中的部门和提问内容
    for context in contexts:
        seg_list = jieba.cut_for_search(context[0])  # 分词
        for seg in seg_list:
            if seg in words:
                continue
            else:
                name_value = ':'.join([context[1], seg])
                # print(name_value)
                # if redisdriver.key_exists(name_value) == 0:
                redisdriver.department_fre_set(name_value, 1, nx=True)  # 部门：词不存在是加入redis，计数一 nx=True
                # else:
                # n = int(redisdriver.department_fre_get(name_value)) + 1
                # print(n)
                redisdriver.department_fre_set(name_value, int(redisdriver.department_fre_get(name_value)) + 1,
                                               xx=True)
                # 部门：词存在时，计数加一 xx=True
    keys = redisdriver.keys_get()  # 获取所有redis中的key
    words = ''  # 用来存放词
    frequencys = ''  # 用来存放词频
    department = ''
    for key in keys:
        department_word = key.decode().split(':')  # 把部门和词分开
        frequency = redisdriver.department_fre_get(key).decode()
        # print(department_word, ' ', frequency)
        if department == '':  # 如果部门为空
            department = department_word[0]  # 把部门写入
            words = department_word[1]  # 把词写入
            frequencys = redisdriver.department_fre_get(key).decode()  # 把词频写入
        elif department == department_word[0]:  # 如果当前写入部门与当前部门相同
            words = words + ',' + department_word[1]
            frequencys = frequencys + ',' + redisdriver.department_fre_get(key).decode()
        else:  # 如果当前写入部门与当前部门不相同
            insert_department_word_frequency(department=department, word=words, frequency=frequencys)  # 把部门、词、词频写入数据库
            department = department_word[0]
            words = department_word[1]  # 把词写入
            frequencys = redisdriver.department_fre_get(key).decode()  # 把词频写入
    print('第一次数据处理完成')


def deal_department_word_frequecy():
    file = open('../data/deal/context_percent.txt', mode='w+', encoding='utf-8')
    department_word_frequency = select_all_department_word_frequency()
    departments = ''
    words = ''
    frequencys = ''
    for department, word, frequency in department_word_frequency:
        if departments == '':
            departments = department
            words = word
            frequencys = frequency
        elif department != departments:
            strs = departments, '===', words, '===', frequencys, '\n'
            file.writelines(str)
            # insert_department_word_frequency(departments, words, frequencys)
            # print(departments, '===', words, '===', frequencys)
            departments = department
            words = word
            frequencys = frequency
        else:
            words = words + ',' + word
            frequencys = frequencys + ',' + frequency
    print('第二次书数据处理完成')


# 每条数据的类别、词、权重
def all_classification_words_weight():
    # context_percent_file = open('../data/deal/context_percent.txt', mode='w+', encoding='utf-8')
    class_file = open('../data/deal/class.txt', 'w+', encoding='utf-8')
    id_title_department_content = sql_select_id_title_department_content()
    categorys = []
    for id, title, context, department in id_title_department_content:
        segments = word_count_dict(context)
        # segments = {}
        # for keyword in jieba.cut(content):
        #     word = keyword.replace(' ', '')
        #     if word not in stop_words and not keyword.isdigit():
        #         if word not in segments:
        #             segments[word] = 1
        #         else:
        #             segments[word] += 1
                # keywords += word + '，'
        # print(segments)
        classification = None
        if '<' in title:    # 从标题下得到类别
            classification = title.split('<')[1].split('>')[0]
            if classification not in categorys:
                categorys.append(classification)
        keywords, frequencys = '', ''
        for keyword, frequency in segments.items():
            if keyword not in STOPWORD:
                keywords += keyword + ','
                frequencys += str(frequency) + ','
        # if classification is None:    # debug时打印
        #     strs = str(id), '\t', '===', '\t', department, '\t', keywords, '\t', str(frequencys), '\n'
        # else:
        #     strs = str(id), '\t', classification, '\t', department, '\t', keywords, '\t', str(frequencys), '\n'
        # print(strs)
        # context_percent_file.writelines(strs)
        insert_id_word_frequency(id=id, classification=classification, word=keywords, frequercy=frequencys)
    for category in categorys:
        class_file.writelines(category + '\n')
    print('每条数据的类别、词、权重')


# 每个部门的词权重
def all_department_weight():
    # file = open('../data/deal/context_percent.txt', mode='w+', encoding='utf-8')
    id_department_content = sql_select_id_department_content()
    contents = ''
    departments = ''
    ids = 1
    for id, content, department in id_department_content:
        if departments == '':
            departments = department
            contents = content
        elif departments == department:
            try:
                contents += str(content)
            except Exception as e:
                print(e)
        else:
            keywords, weights = '', ''
            for keyword, weight in analyse.textrank(contents, topK=50, withWeight=True):
                if keyword not in STOPWORD:
                    keywords += keyword + ','
                    weights += str(weight) + ','
            # strs = str(ids), '\t', departments, '\t', keywords, '\t', weights, '\n'
            insert_department_word_frequency(department=departments, word=keywords, weight=weights)
            # print(strs)
            # file.writelines(strs)
            departments = department
            contents = content
            ids += 1
    keywords, weights = '', ''
    for keyword, weight in analyse.textrank(contents, topK=50, withWeight=True):
        if keyword not in STOPWORD:
            keywords += keyword + ','
            weights += str(weight) + ','
    insert_department_word_frequency(department=departments, word=keywords, weight=weights)
    print('每个部门的词权重')


# 类别、数量、词、 权重
def all_classification_weight():
    for a in redisdriver.keys_get():  # 清理redis
        redisdriver.driver().delete(a)
    class_file = open('../data/deal/class.txt', 'r+', encoding='utf-8')
    title_context = sql_select_classification_context()
    categorys = {}
    for classification, context in title_context:
        if classification is not None:
            # print(classification)
            exist = redisdriver.key_exists(classification)
            # print(exist)
            if exist == 0:
                categorys[classification] = 1
                redisdriver.classification_weight_set(classification, context)
            elif exist == 1:
                categorys[classification] += 1
                context += redisdriver.value_get(classification).decode()
                # print(redisdriver.value_get(classification).decode())
                redisdriver.classification_weight_set(classification, context)
        else:
            continue
    for b in redisdriver.keys_get():
        one_classification = b.decode()
        all_classification_context = redisdriver.value_get(b).decode()
        keywords, weights = '', ''
        for keyword, weight in analyse.textrank(all_classification_context, topK=600, withWeight=True):
            if keyword not in STOPWORD:
                keywords += keyword + ','
                weights += str(weight) + ','
        sql_insert_classification_weight(one_classification, categorys[one_classification], keywords, weights)
    print('类别、数量、词、 权重')


if __name__ == "__main__":
    all_classification_words_weight()
    all_department_weight()
    all_classification_weight()
