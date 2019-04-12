"""
    Author : sorker
    Time: 2019/4/12 15:57
    Desc: This is a Desc
    PRODUCTNAME: PyCharm
"""

from selenium import webdriver
from config import URL

class ChromeDriver():
    def driver(self):
        option = webdriver.ChromeOptions()
        chromedriver = webdriver.Chrome()
        return chromedriver

chromedriver = ChromeDriver()

if __name__ == '__main__':
    driver = chromedriver.driver()
    driver.get(URL)
