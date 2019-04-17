from urllib import request, error, parse
from SqlDeal.sqlcomplaintrawdata import sql_selete_title
import cpca


def get_area_in_txt():
    # 获取网页内容
    file = open('../data/deal/titles.txt', mode='w+', encoding='utf-8')
    titles = sql_selete_title()
    for title in titles:
        title = title[0]
        if len(title) > 50:
            title = title[0:49]
        file.writelines(title + '\n')
        print(title)


def get_area_out_txt():
    file = open('../data/deal/titles.txt', mode='r', encoding='utf-8')
    titles = []
    for title in file.readlines():
        titles.append(str(title).splitlines()[0])
    df = cpca.transform(titles, cut=False, lookahead=3)
    print(df)


if __name__ == "__main__":
    get_area_out_txt()
