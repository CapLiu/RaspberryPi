# -*- coding=utf-8 -*-
from wxbot import *
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

class Systembot(WXBot):
    CHROME_DRIVER_PATH='D:\\WebDrivers\\chromedriver_win32\\chromedriver.exe'
    channel_list=[]
    channel_dict={}
    driver=None
    def __init__(self):
        WXBot.__init__(self)
        self.usr_name = 'self'

    def set_dict(self):
        option=webdriver.ChromeOptions()
        option.add_argument('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
        option.add_extension('2.3.8_0.crx')
        option.add_extension('cntvLive_20160119.crx')
        channel_file=open('channellink.txt','r')
        self.driver=webdriver.Chrome(executable_path=self.CHROME_DRIVER_PATH,chrome_options=option)
        handles=self.driver.window_handles
        curr_handle=self.driver.current_window_handle
        for h in handles:
            if h!=curr_handle:
                self.driver.switch_to.window(h)
                self.driver.close()
        self.driver.switch_to.window(curr_handle)
        self.driver.maximize_window()
        self.channel_dict['1']=['http://tv.cctv.com/live/cctv1/','CCTV-1']
        self.channel_dict['2']=['http://tv.cctv.com/live/cctv2/','CCTV-2']
        self.channel_dict['3'] = ['http://tv.cctv.com/live/cctv3/','CCTV-3']
        self.channel_dict['4'] = ['http://tv.cctv.com/live/cctv4/','CCTV-4']
        self.channel_dict['5'] = ['http://tv.cctv.com/live/cctv5/','CCTV-5']
        self.channel_dict['6'] = ['http://tv.cctv.com/live/cctv6/','CCTV-6']
        self.channel_dict['7'] = ['http://tv.cctv.com/live/cctv7/','CCTV-7']
        self.channel_dict['8'] = ['http://tv.cctv.com/live/cctv8/','CCTV-8']
        self.channel_dict['9'] = ['http://tv.cctv.com/live/cctvjilu/','CCTV-9']
        self.channel_dict['10'] = ['http://tv.cctv.com/live/cctv10/','CCTV-10']
        self.channel_dict['11'] = ['http://tv.cctv.com/live/cctv11/','CCTV-11']
        self.channel_dict['12'] = ['http://tv.cctv.com/live/cctv12/','CCTV-12']
        self.channel_dict['13'] = ['http://tv.cctv.com/live/cctv13/','CCTV-13-新闻']
        self.channel_dict['14'] = ['http://tv.cctv.com/live/cctvchild/','CCTV-14-少儿']
        self.channel_dict['15'] = ['http://tv.cctv.com/live/cctv15/','CCTV-15-音乐']
        self.channel_dict['16'] = ['http://tv.cctv.com/live/cctv5plus/','CCTV-5+']
        for line in channel_file:
            self.channel_dict[line.split(' ')[0]]=[line.split(' ')[1],' ']
        channel_file.close()

    def schedule(self):
        pass
        self.channel_dict.h

    def handle_msg_all(self, msg):
        if msg['msg_type_id']==1:
            if self.channel_dict.has_key(msg['content']['data']):
                self.driver.get(self.channel_dict[msg['content']['data']][0])
                if int(msg['content']['data'])<17:
                    WebDriverWait(self.driver,3).until(lambda x:self.driver.find_element_by_id('hds_flash_player'))
                    video = self.driver.find_element_by_id('hds_flash_player')
                else:
                    WebDriverWait(self.driver, 3).until(lambda x: self.driver.find_element_by_id('vplayer'))
                    video = self.driver.find_element_by_id('vplayer')
                time.sleep(5)
                ActionChains(self.driver).double_click(video).perform()
                ActionChains(self.driver).double_click(video).perform()
            if unicode(msg['content']['data']) == u'get':
                self.set_dict()
            elif unicode(msg['content']['data']) == u'full':
                try:
                    video = self.driver.find_element_by_id('hds_flash_player')
                except NoSuchElementException:
                    video = self.driver.find_element_by_id('vplayer')
                ActionChains(self.driver).double_click(video).perform()
                ActionChains(self.driver).double_click(video).perform()
            elif unicode(msg['content']['data']) == u'exit':
                self.driver.quit()
                sys.exit(0)



