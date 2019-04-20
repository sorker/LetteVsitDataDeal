"""
    Author : sorker
    Time: 2019/4/12 15:57
    Desc: This is a Desc
    PRODUCTNAME: PyCharm
"""

from selenium import webdriver
from config import URL, URL_TEST


class ChromeDriver:
    @staticmethod
    def driver():
        chromedriver = webdriver.Chrome()
        return chromedriver

    @staticmethod
    def driver_options():
        options = webdriver.ChromeOptions()
        options.headless = True
        chromedriver = webdriver.Chrome(options=options)
        return chromedriver


if __name__ == '__main__':
    # driver = chromedriver.driver()
    driver = ChromeDriver.driver_options()
    driver.get(URL_TEST)
