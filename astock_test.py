#利润表=lrb，资产负债表=zcfzb，现金流量表=xjllb
#参考 https://zhuanlan.zhihu.com/p/44753154

import os
import requests, urllib
import xlwt
from bs4 import BeautifulSoup
from time import sleep

stock = input('输入您要查询的股票代码:')
print(stock)

if not os.path.exists('./%s'%stock):
    os.mkdir('./%s'%stock)

lrb_url = 'http://quotes.money.163.com/service/lrb_' + str(stock) + '.html'
zcfzb_url = 'http://quotes.money.163.com/service/zcfzb_' + str(stock) + '.html'
xjllb_url = 'http://quotes.money.163.com/service/xjllb_' + str(stock) + '.html'
path = './%s/'%stock

def lrb():
    while True:
        try:
            content = urllib.request.urlopen(lrb_url, timeout=2).read()
            with open(path+'lrb.csv','wb') as f:
                f.write(content)
            print(content)
            sleep(1)
            break
        except Exception as e:
            if str(e) == 'HTTP Error 404: Not Found':
                break
            else:
                print(e)
                continue

def zcfzb():
    while True:
        try:
            content = urllib.request.urlopen(zcfzb_url, timeout=2).read()
            with open(path+'zcfzb.csv','wb') as f:
                f.write(content)
            print(content)
            sleep(1)
            break
        except Exception as e:
            if str(e) == 'HTTP Error 404: Not Found':
                break
            else:
                print(e)
                continue

def xjllb():
    while True:
        try:
            content = urllib.request.urlopen(xjllb_url, timeout=2).read()
            with open(path+'xjllb.csv','wb') as f:
                f.write(content)
            print(content)
            sleep(1)
            break
        except Exception as e:
            if str(e) == 'HTTP Error 404: Not Found':
                break
            else:
                print(e)
                continue

lrb()
zcfzb()
xjllb()