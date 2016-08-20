# -*- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time,sys,re,urllib2,urllib,cookielib,datetime,requests
import threading
import platform

def GetTodayPicture():
    pic_url="http://cn.bing.com/"
    wb_data=requests.get(pic_url)
    pic_pattern=re.compile(r'http://.*?bing\..*?1080.jpg')
    pic_address=pic_pattern.search(wb_data.text).group()
    filename_pattern=re.compile(r'rb/.*?\.jpg')
    filename=filename_pattern.search(pic_address).group()[4:]
    if platform.system()=='Windows':
        urllib.urlretrieve(pic_address,'D:\\TestData\\BingToday\\'+str(filename))
    elif platform.system()=='Linux':
        urllib.urlretrieve(pic_address,'./BingWallpaper/'+str(filename))
    print "今日图片下载完成。"

if __name__=="__main__":
    GetTodayPicture()
    exit()
