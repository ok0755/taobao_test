#coding=utf-8
import requests
import re
import os
import time

class taobao(object):

    def __init__(self,start,end,goods):
        self.f=open('d:\\taobao2.html','w')  #存储路径
        self.goods=goods
        self.start=start
        self.end=end
        self.i=0
        self.pic_links=[]
        self.getHTMLText(start,end)

    #获取页面函数
    def getHTMLText(self,start,end):
        time.sleep(2)
        start_url=r'https://s.taobao.com/search?q={}&sort=sale-desc'.format(self.goods)
        for k in range(start,end):
            url='{}&s={}'.format(start_url,str(44*k))
            r=requests.get(url,timeout=20)
            html=r.text
            r.close()
            self.parsePage(html)

    #对获取页面进行解析，正则匹配
    def parsePage(self,html):
        recompile=re.compile(r'"nid":"(.*?)".*?"raw_title":"(.*?)","pic_url":"(.*?)","detail_url":"(.*?)","view_price":"(.*?)".*?"item_loc":"(.*?)","view_sales":"(.*?)","comment_count":"(.*?)","user_id":"(.*?)","nick":"(.*?)"',re.S)
        try:
            results=re.findall(recompile,html)
            self.write2Html(results)
        except:
            pass

    #写入文件，生成html
    def write2Html(self,results):
        for lis in results:
            self.i+=1
            self.f.write('<table><tr><td><img src="http:{}" width="200"></td>\n'.format(lis[2].encode('utf-8')))  #商品图片
            self.f.write('<td>序号:--{}<br/>\n'.format(self.i))
            link=lis[3].decode('unicode_escape').encode('utf-8')    #商品链接
            self.f.write('<a href="http:{}">店址：--http:{}</a><br/>\n'.format(link,link))
            self.f.write('商品名:--{}<br/>\n'.format(lis[1].encode('utf-8')))
            self.f.write('<font color="red">价格:--{}</font><br/>\n'.format(lis[4].encode('utf-8'))) #价格
            self.f.write('地址:--{}<br/>\n'.format(lis[5].encode('utf-8')))
            self.f.write('销量:--{}<br/>\n'.format(lis[6].encode('utf-8')))
            self.f.write('评论数:--{}<br/>\n'.format(lis[7].encode('utf-8')))
            self.f.write('卖家昵称:--{}</table><br/></td></tr></table>\n'.format(lis[9].encode('utf-8')))
            self.get_comment(lis[0],lis[8])
            self.download_goods_pics(link)

    def get_comment(self,nid,userid):  #获取商品评价第一页
        url='https://rate.tmall.com/list_detail_rate.htm?itemId={}&sellerId={}&currentPage=1'.format(nid,userid)
        res=requests.get(url)
        html=res.text
        res.close()
        detail=re.compile('"rateContent":"(.*?)"',re.S)
        for txt in re.findall(detail,html):
            self.f.write('<font color="0000FF">评价:{}</font><br/>\n'.format(txt.encode('utf-8'))) #写入
        self.f.write('<hr>')  #插分隔线

    def download_goods_pics(self,url):
        time.sleep(1)
        res=requests.get('http:'+url)
        html=res.text
        res.close()
        try:
            pic_sources=re.compile('(//dsc.taobaocdn.com.*?)(\"|\')',re.S)  #图片上级地址
            pic_urls='http:{}'.format(re.search(pic_sources,html).group(1))
            self.pic_links.append(pic_urls)
        except:
            pass

if __name__=='__main__':
    goods=raw_input('enter keywords:>>>').encode('utf-8')
    taobao(0,1,goods)
