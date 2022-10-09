# coding:utf-8
import time

import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                             ' (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'
               }
    kw = input('enter a word:')
    param = {
        'keyword': kw
    }
    response = requests.get(url, params=param, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return


def get_infos(html):
    html = BeautifulSoup(html, "html.parser")
    num = html.select('#wrapper > div > div > div > ol.grid_view > li > div.item > div.pic > em')
    title = html.select('#wrapper > div> div > div> ol.grid_view > li > div.item > div.info'
                        ' > div.hd > a > span.title:nth-child(1)')
    link = html.select('#wrapper > div > div > div > ol.grid_view > li > div.item > div.pic > a ')
    rating_num = html.select('#wrapper > div > div > div.article > ol.grid_view > li'
                             ' > div.item > div.info > div.bd > div.star>span.rating_num')
    evaluate_number = html.select('#wrapper > div > div > div.article > ol.grid_view > li'
                                  ' > div.item > div.info > div.bd > div.star>span:nth-child(4)')
    for n, t, l, r, e in zip(num, title, link, rating_num, evaluate_number):
        n = n.get_text().replace('\n', '').replace('\t', '').replace('\r', '')
        t = t.get_text()
        r = r.get_text()
        e = e.get_text().replace('\n', '').replace('\t', '').replace('\r', '')
        data = {
            '排名': n,
            '电影名字': t,
            '链接': l,
            '评分': r,
            '评分人数': e
        }
        print(data)


def main():
    urls = ['https://search.bilibili.com/all'.format(str(i)) for i in range(0, 226, 25)]
    for url in urls:
        html = get_html(url)
        get_infos(html)
        # break
        time.sleep(0.5)


if __name__ == '__main__':
    main()
