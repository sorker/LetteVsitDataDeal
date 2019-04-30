# -*- coding:utf-8 -*-
"""
Author : sorker
Time: 2019/4/12 16:04 
Desc: This is a Desc
Product: PyCharm  
"""
from selenium.webdriver.common.by import By

URL = 'http://zxts.zjzwfw.gov.cn/wsdt.do?method=sunshine'   # 网址
URL_TEST = 'http://www.baidu.com' # 测试地址

ELEMENT_CLICK_ORDER = {
    By.CLASS_NAME: 'delete',
}   # 点击网页的元素的顺序

ELEMENT_TITLE_CONTENT = [By.XPATH, '//table[@class="tablelist1"]/tbody/tr']  # 获取标题和时间


STOPWORD = open('../data/停用词表.txt', mode='r+', encoding='utf-8').read()
