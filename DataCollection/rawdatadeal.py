from urllib import request, error, parse
from config import URL, URL_TEST



def get_area_in_txt(url):
    # 获取网页内容
    page = request.urlopen(url)
    html = page.read().decode('utf-8')
    return html

if __name__ == "__main__":
    pass
