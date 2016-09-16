#-*- coding=utf-8 -*-
from wxbot import WXBot


class MissionWorker:
    def __init__(self):
        self.bot=WXBot()
        self.send_to=''
        self.noticeContent=''

    def set_notice_content(self,content):
        self.noticeContent=content

    def set_sendto(self,sendto_name):
        self.send_to=sendto_name

    def send_notice(self):
        if self.send_to=='':
            self.bot.sendnotice(self.noticeContent)
        else:
            self.bot.sendnotice(self.noticeContent,self.send_to)

    def do(self):
        #做实际任务，重载即可
        pass

    def startwork(self):
        self.bot.showqrcode()
        self.do()
        self.send_notice()