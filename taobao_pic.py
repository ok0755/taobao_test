#coding=utf-8
from taobao import taobao

class taobao_pic(taobao):
    def __init__(self,links):
        super(taobao_pic,self).__init__(self.start,self.end,self.goods)
        self.header={'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'}
        self.open_pic_url()

    def open_pic_url(self):
        for pic_url in self.pic_links:
            print pic_url

if __name__=='__main__':
    goods=raw_input('enter keywords:>>>').encode('utf-8')
    test=taobao(0,1,goods)
    pics=test.pic_links
    taobao_pic(pics)

