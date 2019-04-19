from urllib import request, error, parse
from SqlDeal.sqlcomplaintrawdata import sql_selete_title
import cpca


def get_area_in_txt():
    # 获取网页内容
    file = open('../data/deal/titles.txt', mode='w+', encoding='utf-8')
    titles = sql_selete_title()
    for title in titles:
        title = title[0]
        # if len(title) > 50:
        #     title = title[0:49]
        file.writelines(title + '\n')
        # print(title)


def get_area_out_txt():
    file = open('../data/deal/titles.txt', mode='r', encoding='utf-8')
    area_out = open('../data/deal/area_out.txt', mode='w+', encoding='utf-8')
    titles = []
    for title in file.readlines():
        titles.append(str(title).splitlines()[0])
    df = cpca.transform(titles, cut=False, lookahead=3)
    area_out.writelines('ID' + '\t' + '省' + '\t' + '市' + '\t' + '区' + '\t' + '地址' + '\n')
    for index, rows in df.iterrows():
        row = str(index) + '\t' + rows['省'] + '\t' + rows['市'] + '\t' + rows['区'] + '\t' + rows['地址'] + '\n'
        area_out.writelines(row)

def get_context_out_text():
    file = open('../data/deal/titles.txt', mode='r', encoding='utf-8')


if __name__ == "__main__":
    get_area_in_txt()
    get_area_out_txt()
