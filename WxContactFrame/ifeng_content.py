# -*- coding=utf-8 -*-
from bs4 import BeautifulSoup
from content_obtainer import obtainer
import requests,re,sys
import time,datetime
reload(sys)

class ifeng_obtainer(obtainer):

    def obtain_content(self):
        wbtext=requests.get(self.url)
        wbtext.encoding='utf-8'
        soup=BeautifulSoup(wbtext.text,'lxml',from_encoding='UTF-8')
        headline=soup.select('#headLineDefault > h1 > a')
        headline=unicode(headline[0].string)+' '+unicode(headline[0]['href'])+'\n'
        important_news=soup.select('#headLineDefault > ul > li > a')
        important_news_content=[]
        re_content=re.compile(r'>.*?<')
        re_href=re.compile(r'href=".*?"')

        final_content='北京时间：'+str(datetime.datetime.now())+'\n今日要闻：\n'+headline
        for news in important_news:
            #print news
            if 'class="strong"' in str(news):
                important_news_content.append(news)
                content=re_content.search(str(news)).group(0)[1:-1]
                link=re_href.search(str(news)).group(0).split('=')[1]
                final_content=final_content+content+' '+link+'\n'
        self.setcontent(final_content)
        #print final_content


