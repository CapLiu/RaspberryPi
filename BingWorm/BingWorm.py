# -*- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time,sys,re,urllib2,urllib,cookielib,datetime,requests
import threading


CHROMEDRIVER_PATH='D:\\WebDrivers\\chromedriver_win32\\chromedriver.exe'
PHANTOMJS_PATH='D:\\WebDrivers\\phantomjs\\bin\\phantomjs.exe'
class BingWorm:
    url=""
    driver=None
    pictures=[]
    dates=[]
    url_list=[]
    sub_url_list=[]
    threads=[]
    thread_count=1
    def __init__(self):
        self.url="http://www.bing.com/gallery/"
        self.driver=webdriver.PhantomJS(executable_path=PHANTOMJS_PATH)
        #self.driver=webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)

    def GetTodayPicture(self):
        pic_url="http://cn.bing.com/"
        wb_data=requests.get(pic_url)
        pic_pattern=re.compile(r'http://.*?bing\..*?1080.jpg')
        pic_address=pic_pattern.search(wb_data.text).group()
        filename_pattern=re.compile(r'rb/.*?\.jpg')
        filename=filename_pattern.search(pic_address).group()[4:]
        urllib.urlretrieve(pic_address,'D:\\TestData\\BingToday\\'+str(filename))
        print "今日图片下载完成。"

    def GetPictures(self):#获取图片地址
        self.driver.get(self.url)
        js = "document.body.scrollTop=document.body.scrollHeight"
        for i in range(0,10):
            self.driver.execute_script(js)
            time.sleep(1)
        time.sleep(3)
        self.pictures=self.driver.find_elements_by_class_name("tileBg")
        print "请稍后……"
        for picture in self.pictures:
            urls=str(picture.get_attribute("src")).replace("640x360","1920x1200").replace("320x180", "1920x1200")
            self.url_list.append(urls)
        self.driver.close()
    def TaskArrange(self,n):#n为线程数
        self.thread_count=n
        task_list_count=len(self.url_list)/self.thread_count
        for i in range(0,len(self.url_list),task_list_count):
            self.sub_url_list.append(self.url_list[i:i+task_list_count])
        #print self.sub_url_list
    def DownLoadPic(self,piclist):
        for picurl in piclist:
            filename_pattern=re.compile(r'files/.*?\.jpg')
            picname=filename_pattern.search(picurl).group()[6:]
            urllib.urlretrieve(picurl,"D:\\TestData\\Bing\\"+str(picname)+".jpg")
            print str(picname)+"下载完成。"

    def DownLoad(self):
        for i in range(0,len(self.sub_url_list)):
            self.threads.append(threading.Thread(target=self.DownLoadPic,args=(self.sub_url_list[i],)))
        for t in self.threads:
            t.start()
if __name__=="__main__":
    worm=BingWorm()
    #worm.GetTodayPicture()
    worm.GetPictures()
    worm.TaskArrange(10)
    worm.DownLoad()
    exit()
