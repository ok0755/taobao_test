#coding=utf-8
import requests
import re
import os
import time
#获取页面函数、
def getHTMLText(url):
    time.sleep(1)
    try:
        r=requests.get(url,timeout=15)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        pass

#对获取页面进行解析
def parsePage(ilt,html):
    try:
		#在爬取下来的网页中进行查找价格
        plt=re.findall(recompile,html)
        ar.append(plt)
    except:
        pass
    return ar

def main():
    #time.sleep(1)
    goods='荣耀9'  #可以自定义搜索关键字
    depth=2           #截取前2页,可以任意定义爬取页数
    start_url=r'https://s.taobao.com/search?q={}&sort=sale-desc'.format(goods)
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            lists=parsePage(infoList , html)
            wr(lists)
        except:
            continue

def wr(lists):
    i=0
    for list_ in lists:
        for lis in list_:
            i+=1
            f.write('序号:--{}<br/>'.format(i))
            li=lis[2].decode('unicode_escape').encode('utf-8')
            f.write('<a href="http:{}">店址：--http:{}</a><br/>'.format(li,li))
            f.write('商品名:--{}<br/>\n'.format(lis[0].encode('utf-8')))
            f.write('<font color="red">价格:--{}</font><br/>\n'.format(lis[3].encode('utf-8')))
            f.write('地址:--{}<br/>\n'.format(lis[4].encode('utf-8')))
            f.write('销量:--{}<br/>\n'.format(lis[5].encode('utf-8')))
            f.write('评论数:--{}<br/>\n'.format(lis[6].encode('utf-8')))
            f.write('卖家ID:--{}<br/>\n'.format(lis[7].encode('utf-8')))
            f.write('<img src="http:{}" width="200"><br/>\n'.format(lis[1].encode('utf-8')))
            f.write('<hr>')

if __name__=='__main__':
    f=open('d:\\taobao.html','w')  #存储路径
    '''
    raw_title 商品名
    pic_url 商品图
    detail_url 商品详页
    view_price 价格
    item_loc 发货地址
    view_sales 销量
    comment_count  评论数
    nick  卖家ID
    '''
    recompile=re.compile('"raw_title":"(.*?)".*?"pic_url":"(.*?)".*?"detail_url":"(.*?)".*?"view_price":"(.*?)".*?"item_loc":"(.*?)".*?"view_sales":"(.*?)".*?"comment_count":"(.*?)".*?"nick":"(.*?)"',re.S)
    ar=[]
    main()
    f.close()
