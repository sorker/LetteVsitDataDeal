"""
Author : sorker
Time: 2019/4/12 16:14 
Desc: This is a Desc
Product: PyCharm  
"""

from WebDriver.chromedriverOption import chromedriver
from config import URL, ELEMENT_DICT

driver = chromedriver.driver()

class Registeration():
    def click_time(self):
        for by, vlaue in ELEMENT_DICT.items():
            self.element_click(by, vlaue)

    def element_click(self, by, value):
        element = driver.find_element(by, value)
        element.click()
        driver.current_url()

if __name__ == '__main__':
    driver.get(URL)
    Registeration().click_time()

