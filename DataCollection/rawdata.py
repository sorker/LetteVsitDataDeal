from urllib import request, error, parse
from WebDriver.chromedriverOption import driver
from config import URL, URL_TEST

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
           'Accept': r'application/json, text/javascript, */*; q=0.01', }

def getHtml(url):
    # 获取网页内容
    page = request.urlopen(url)
    html = page.read().decode('utf-8')
    return html

if __name__ == "__main__":
    print(getHtml(URL_TEST))
