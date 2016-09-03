#-*- coding=utf-8 -*-
from wxbot import WXBot


class MissionWorker:
    def __init__(self):
        self.bot=WXBot()
        self.noticeContent=''

    def set_notice_content(self,content):
        self.noticeContent=content

    def send_notice(self):
        self.bot.sendnotice(self.noticeContent)

    def do(self):
        #做实际任务，重载即可
        pass

    def startwork(self):
        self.bot.showqrcode()
        self.do()
        self.send_notice()