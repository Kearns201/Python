import re
import traceback

import requests
from bs4 import BeautifulSoup


def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        print('Error!')


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            string = re.findall(r'[s][h]\d{6}', href)[0].replace('sh', '')
            if lst == []:
                lst.append(string)
                continue
            if lst[-1] == string:
                continue
            else:
                lst.append(string)
        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    regex_symbol = r'\"symbol\":\"\d{6}\"'
    regex_name = r'\"nameCN\":\".*?\"'
    regex_latestPrice = r'\"latestPrice\":[\d\.]*'
    count = 0
    total_list = []
    for stock in lst:
        url = stockURL + stock
        html = getHTMLText(url)
        try:
            if html == '':
                continue
            stockInfo = []
            for match in re.finditer(regex_symbol, html):
                stockInfo.append(match.group(0).replace("\"symbol\":", ""))
            for match in re.finditer(regex_name, html):
                stockInfo.append(match.group(0).replace("\"nameCN\":", ""))
            for match in re.finditer(regex_latestPrice, html):
                stockInfo.append(match.group(0).replace("\"latestPrice\";", ""))

            with open(fpath, 'a', encoding='utf-8') as f:
                tmpl = '{0:^10}{1:{3}^6}{2:^8}\n'
                if count == 0:
                    string = tmpl.format('代码', '股票名称', '最新价', chr(12288))

                else:
                    print('\r当前进度:{:.2f}%'.format(count * 100 / len(lst)), end='')
                    string = tmpl.format(str(stockInfo[0]).replace('\"', ''), str(stockInfo[1].replace('\"', '')),
                                         str(stockInfo[2]), chr(12288))
                f.write(string)
            count += 1
        except:
            traceback.print_exc()
            continue


if __name__ == '__main__':
    stock_list_html = 'http://app.finance.ifeng.com/list/stock.php?t=ha&f=chg_pct&o=desc&p=1'
    stock_info_url = 'https://www.laohu8.com/stock/'
    output_file = 'D://StockLista.txt'
    slist = []
    getStockList(slist, stock_list_html)
    getStockInfo(slist, stock_info_url, output_file)
