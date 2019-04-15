"""
Author : sorker
Time: 2019/4/12 16:14 
Desc: This is a Desc
Product: PyCharm  
"""

from WebDriver.chromedriverOption import chromedriver
from config import URL, ELEMENT_CLICK_ORDER, ELEMENT_TITLE_CONTENT
import re
from time import sleep
from SqlDeal.sqlcomplaintrawdata import sql_insert_complaintrawdata

driver = chromedriver.driver()


class Registeration():
    def click_time(self):   # 按顺序点击
        for by, vlaue in ELEMENT_CLICK_ORDER.items():
            self.element_click(by, vlaue)

    def element_click(self, by, value):     # 点击事件
        element = driver.find_element(by, value)
        element.click()
        # driver.current_url()

    def title_compare_context(self):
        titles = []
        elements_title = driver.find_elements(ELEMENT_TITLE_CONTENT[0], ELEMENT_TITLE_CONTENT[1])
        for element in elements_title:
            try:
                trs = element.get_attribute('outerHTML')
                tds = str(trs).split('<td>')
                title = tds[0].split('\"')[3]
                content = str(element.text).split(' ')[0]
                if title == content and title is not None:
                    i = 0
                    for k in titles:
                        if k[0] == title:
                            i = i + 1
                    titles.append([title, i])    # 返回标题、 标题重复数量
            except Exception as e:
                continue
        return titles

    def click_title_switch_ifarme(self, title, title_count, i):
        """
        :param title: 标题
        :param title_count: 标题重复数量
        :param i: 标题顺序
        :return: 标题，获取内容, 获取反映时间, 获取答复单位, 获取答复时间, 获取答复意见
        """
        content = []
        try:
            elements = driver.find_elements_by_xpath('//table[@class="tablelist1"]/tbody/tr/td[@title="' + title + '"]')
            # 按标题获取元素组
            elements[title_count].click()  # 按重复顺序选择元素点击
            driver.switch_to.frame('layui-layer-iframe' + str(i))
            span_elements = driver.find_elements_by_tag_name('span')
            content.append(title)
            content.append(span_elements[2].text)   # 获取内容
            content.append(span_elements[3].text)   # 获取反映时间
            content.append(span_elements[5].text)   # 获取答复单位
            content.append(span_elements[6].text)   # 获取答复时间
            content.append(span_elements[7].text)   # 获取答复意见
            driver.switch_to.default_content()
            driver.find_element_by_xpath('//span[@class="layui-layer-setwin"]/a').click()  # 点击关闭弹窗
        except Exception as e:
            pass
        return content

    def loop_titles(self, titles):
        contents = []
        for k, title in enumerate(titles):
            content = Registeration().click_title_switch_ifarme(title[0], title[1], k + 1)
            contents.append(content)
        return contents


if __name__ == '__main__':
    driver.get(URL)
    Registeration().click_time()
    titles = Registeration().title_compare_context()
    contents = Registeration().loop_titles(titles)
    for content in contents:
        sql_insert_complaintrawdata(content[0], content[1], content[2], content[3], content[4], content[5])
    print(contents)
    print(len(contents))
