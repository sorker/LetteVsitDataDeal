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
from SqlDeal.sqlcityarea import select_city_area


class Registeration:
    def __init__(self, driver):
        self.driver = driver

    def click_time(self):  # 按顺序点击
        for by, vlaue in ELEMENT_CLICK_ORDER.items():
            self.element_click(by, vlaue)

    def element_click(self, by, value):  # 点击事件
        element = self.driver.find_element(by, value)
        element.click()
        # self.driver.current_url()

    def title_compare_context(self):
        titles = []
        elements_title = self.driver.find_elements(ELEMENT_TITLE_CONTENT[0], ELEMENT_TITLE_CONTENT[1])
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
                    titles.append([title, i])  # 返回标题、 标题重复数量
            except Exception as e:
                print('title_compare_context: ', e)
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
            elements = self.driver.find_elements_by_xpath(
                '//table[@class="tablelist1"]/tbody/tr/td[@title="' + title + '"]')
            # 按标题获取元素组
            elements[title_count].click()  # 按重复顺序选择元素点击
            self.driver.switch_to.frame('layui-layer-iframe' + str(i))
            span_elements = self.driver.find_elements_by_tag_name('span')
            if len(title) > 100:
                title[0:99]
            content.append(title)
            content.append(span_elements[2].text)  # 获取内容
            content.append(span_elements[3].text)  # 获取反映时间
            content.append(span_elements[5].text)  # 获取答复单位
            content.append(span_elements[6].text)  # 获取答复时间
            content.append(span_elements[7].text)  # 获取答复意见
            self.driver.switch_to.default_content()
            self.driver.find_element_by_xpath('//span[@class="layui-layer-setwin"]/a').click()  # 点击关闭弹窗
        except Exception as e:
            try:
                self.driver.find_element_by_xpath('//span[@class="layui-layer-setwin"]/a').click()
            except Exception:
                pass
            print('click_title_switch_ifarme: ', e)
            pass
        return content

    def loop_titles(self):
        """
        :desc: 循环获取该页面十条数据
        :return:
        """
        contents = []
        titles = self.title_compare_context()
        for k, title in enumerate(titles):
            try:
                content = self.click_title_switch_ifarme(title[0], title[1], k + 1)
            except Exception as e:
                print('loop_titles：', e)
                continue
            contents.append(content)
        return contents

    def next_page(self, city, area):
        """
        :desc: 循环获取每页的数据
        :return:
        """
        elements = self.driver.find_elements_by_class_name('paginItem')
        for i in range(10):
            elements[i + 1].click()
            try:
                contents = self.loop_titles()
                for content in contents:
                    sql_insert_complaintrawdata(content[0], content[1], content[2], content[3], content[4], content[5],
                                                city, area)
                    # 把每条数据写入数据库
                elements = self.driver.find_elements_by_class_name('paginItem')
            except Exception as e:
                print('next_page: ', e)
                continue

    def next_area(self):
        """
        :desc: 循环获取每个地点的数据
        :return:
        """
        self.driver.get(URL)
        self.click_time()
        for id, city, area in select_city_area():
            # print(id, city, area)
            try:
                print(city, ', ', area)
                self.driver.find_element_by_id('city').send_keys(city)
                sleep(1)
                self.driver.find_element_by_id('county').send_keys(area)
                sleep(1)
                self.driver.find_element_by_class_name('getSmsCode2').click()
                sleep(1)
                self.next_page(city, area)
            except Exception as e:
                print('next_area: ', e)
                continue
            if id == 10:
                break
        # drive.close()


drive = chromedriver.driver()
registeration = Registeration(drive)

if __name__ == '__main__':
    # driver_options = chromedriver.driver_options()
    registeration.next_area()
