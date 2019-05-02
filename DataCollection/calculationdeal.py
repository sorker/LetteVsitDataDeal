# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/30 14:21
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
import cpca
import jieba
import os
from jieba import analyse
from ConDriver.redisdriver import redisdriver
import operator
from SqlDeal.sqlcomplaintrawdata import sql_select_classification_weight, sql_select_department, sql_select_department_weight
from config import STOPWORD, DATA_DIR


def class_sort(context):   # 分类
    classification_words_weights = sql_select_classification_weight()
    segments = word_count_dict(context)
    class_dir = os.path.join(DATA_DIR, '类别.txt')
    classifications = open(class_dir, 'r', encoding='utf-8').readline().split(',')
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
                    match += float(weight) * segments[word]
                else:
                    continue
        except Exception as e:
            print(e)
        classifications_match[classification] = match
    sorted_classifications_match = sorted(classifications_match.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_classifications_match


def word_count_dict(context):  # 分词并计算词频
    segments = {}
    for keyword in jieba.cut(context):
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
    departments = sql_select_department(city, area)
    department_word_weights = sql_select_department_weight(city, area)
    department_match = {}
    for department in departments:
        match = 0
        # print(classification)
        # try:
        word_weight = department_word_weights[department]
        for word, weight in word_weight.items():  # 如果有则权重相加
            # print(word)
            if segments.__contains__(word):
                # print(department, word)
                # print(segments[word])
                match += float(weight) * segments[word]
            else:
                continue
        # except Exception as e:
        #     print(e)
        department_match[department] = match
    sorted_department_match = sorted(department_match.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_department_match


def tuple_to_dict(tuplex):
    tuple_dict = dict((x, y) for x, y in tuplex)
    return tuple_dict


if __name__ == '__main__':
    context = '杭州市政府领导： 2019年3月4日，******市场监督管理局回应有关浙江天然股权投资基金管理有限公司股权变更的质疑时，称：2018年9月3日，当事人办理股权变更时，玉泉所并未收到任何司法机关和行政机关要求停止办理股权变更的公函，同时，当事人提供了三部门联审单，所以根据《公司法》规定予以办理。 在此，我们对西湖市场监督局快速回应表示赞赏。同时，我们仍旧存在质疑： （1）、市场监督局的职能，是否只是形式审核资料？在西湖区政府信息公开网（http: xxgk.hzxh.gov.cn art 2016 8 6 art_12*****0_27.html），公示了市场监督局职能包括“依法负责对各类市场主体经营行为监督管理;组织开展企业信用体系建设,推进政府企业信用、行业信用建设,实施信用分类管理”等，由一个失信人接手1亿股权款，明显是有违信用建设的。后西湖监督局发现天然基金无法联系，将天然基金列入异常名录，我们表示赞赏。 （2）、作为普通百姓，对政府部门运作，肯定是不甚熟悉。一开始质疑西湖市场监督局，是因为国家企业信用信息系统中显示天然基金的登记机关是西湖市场监督管理局。我们关心的焦点是：天然基金控股的宜湃网，在标的逾期后，让失信人接收股权，从而进一步发展到宜湃平台全线逾期，人员失联的境地。西湖局称的三部门联审单，是哪三个部门，这三个部门分别审核了什么？是不是只是形式审核？ （3）、即使已经失误，股权变更既成事实后，政府部门有没有采取什么挽救措施？ （4）希望各政府职能部门，对待人民的关切，不要抽茧剥丝地回答，要主动提供全方位信息回应。 附：天然基金控股宜湃网全线逾期大致情况： 基金公司全资控股宜湃网& #40;www.yipaiwang.com& #41;。宜湃网引流金交所项目，包括银优计划和企优计划二大金融产品。和宜湃网合作的二大金交所——青岛联合信用资产交易中心和贵州场外机构间市场有限基金公司均于2019年1月向宜湃网案发时的办公所在地——成都经侦报案诈骗。银优计划完全是虚假产品；企优计划无真实的供应链交易，抵押物不足且不易变现。以上情况说明，基金公司设立目的是为诈骗钱财，几乎是一股金融黑组织。 20*****3，修涞贵转出股权，苗田福接手。苗田福是失信人，他承认代持股份，意思就是“背锅”的。而西湖市场监督局允许登记上此次股权转让，事实上为他的“背锅”进行了“背书”。'
    # print(department_sort(context, '杭州',	'上城区'))
    print(tuple_to_dict(class_sort(context)))
