# coding:utf-8

import requests

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70'}
    params = {
        'cname': '',
        'pid': '',
        'keyword': '上海',
        'pageIndex': '1',
        'pageSize': '10',
    }

    response = requests.get(url=url, headers=headers, params=params)
