"""
    Author : sorker
    Time: 2019/4/12 15:57
    Desc: This is a Desc
    PRODUCTNAME: PyCharm
"""

from selenium import webdriver
from config import URL, URL_TEST


class ChromeDriver():
    def driver(self):
        chromedriver = webdriver.Chrome()
        return chromedriver

    def driver_options(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        chromedriver = webdriver.Chrome(options=options)
        return chromedriver


chromedriver = ChromeDriver()

if __name__ == '__main__':
    # driver = chromedriver.driver()
    driver = chromedriver.driver_options()
    driver.get(URL_TEST)
