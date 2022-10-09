# coding:utf-8
import json

import requests

if __name__ == '__main__':
    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.进行UA伪装
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54'
               }
    # 3.post请求参数处理(同get请求一致)
    word = input('enter a word:')
    data = {
        'kw': word
    }
    # 4.请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5.获取响应数据:json()方法返回的是obj(如果确认响应数据的json类型的,才可以使用json())
    dic_obj = response.json()

    # 持久化存储
    fileName=word+'.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print('over!')
