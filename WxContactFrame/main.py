# -*- coding=utf-8 -*-
from Deal import MissionWorker
from ifeng_content import ifeng_obtainer

if __name__=="__main__":
    ifer=ifeng_obtainer('http://www.ifeng.com/')
    ifer.obtain_content()
    worker=MissionWorker()
    worker.set_sendto(u'安定医院精神病室不熄灯')
    worker.set_notice_content(ifer.getcontent())
    worker.startwork()
    exit()
