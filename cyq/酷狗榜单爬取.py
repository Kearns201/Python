# coding:utf-8

import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59'
               }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return


def get_infos(html):
    html = BeautifulSoup(html, "html.parser")
    ranks = html.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
    name = html.select('#rankWrap > div.pc_temp_songlist > ul > li> a')
    time = html.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    for r, n, t in zip(ranks, name, time):
        r = r.get_text().replace('\n', '').replace('\t', '').replace('\r', '')
        n = n.get_text()
        t = t.get_text().replace('\n', '').replace('\t', '').replace('\r', '')
        data = {
            '排名': r,
            '歌名—歌手': n,
            '播放时间': t
        }
        print(data)


def main():
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1, 24)]
    for url in urls:
        html = get_html(url)
        get_infos(html)
        # time.sleep(1)


if __name__ == '__main__':
    main()
