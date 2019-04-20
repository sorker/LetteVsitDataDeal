from urllib import request, error, parse
from SqlDeal.sqlcomplaintrawdata import sql_select_title, sql_select_department_content
from SqlDeal.sqldepartmentwordfrequency import insert_department_word_frequency
from ConDriver.redisdriver import redisdriver
import cpca
import jieba

rabbit = [',', '.', '/', '，', '。', '、', '*', '（', '）', '？', '：',  '了', '你', '我', '他', '你们', '我们', '他们', '吗', '不']


def get_area_in_txt():
    # 获取网页内容
    file = open('../data/deal/titles.txt', mode='w+', encoding='utf-8')
    titles = sql_select_title()
    for title in titles:
        title = title[0]
        # if len(title) > 50:
        #     title = title[0:49]
        file.writelines(title + '\n')
        # print(title)


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


def get_context_out_text():
    # file = open('../data/deal/context_percent.txt', mode='w+', encoding='utf-8')
    contexts = sql_select_department_content()
    for context in contexts:
        seg_list = jieba.cut_for_search(context[0], HMM=True)
        for seg in seg_list:
            try:
                rabbit.index(seg)
                continue
            except Exception as e:
                name_value = ':'.join([context[1], seg])
                # print(name_value)
                # if redisdriver.key_exists(name_value) == 0:
                redisdriver.department_fre_set(name_value, 1, nx=True)  # 部门：词不存在是加入redis，计数一
                # else:
                #     n = int(redisdriver.department_fre_get(name_value)) + 1
                #     # print(n)
                redisdriver.department_fre_set(name_value, int(redisdriver.department_fre_get(name_value)) + 1, nx=True)
                # 部门：词存在时，计数加一
    keys = redisdriver.keys_get()
    words = []
    frequencys = []
    department = ''
    for key in keys:
        department_word = key.decode().split(':')
        print(department_word)
        if department == '':
            department = department_word[0]
            words.append(department_word[1])
            frequencys.append(redisdriver.keys_get(key))
        elif department == department_word[0]:
            words.append(department_word[1])
            frequencys.append(redisdriver.keys_get(key))
        else:
            insert_department_word_frequency(department_word[0], words, frequencys)
            words = []
            frequencys = []
            department = department_word[0]
            words.append(department_word[1])
            frequencys.append(redisdriver.keys_get(key))


if __name__ == "__main__":
    get_context_out_text()
    # get_area_out_txt()
