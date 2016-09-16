# -*- coding=utf-8 -*-
class obtainer:
    def __init__(self,url):
        self.content=''
        self.url=url

    def getcontent(self):
        return self.content

    def setcontent(self,content):
        self.content=content

    def geturl(self):
        return self.url

    def obtain_content(self):
        pass