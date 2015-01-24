#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    下载煎蛋妹子图
    url: http://jandan.net/ooxx
    example of image link:
    <img src="http://ww1.sinaimg.cn/mw600/8074970djw1eiqgynb3y4j20rs14s41z.jpg" style="max-width: 608px; max-height: 450px;">
    author: ch4in
    just4fun.
"""

import sys, urllib, urllib2, time, re, os
from bs4 import BeautifulSoup
import threading, Queue


SAVE_PATH = './img/'
workQueue = Queue.Queue()
_THREAD_NUM = 3 #线程数目

class MyThread(threading.Thread):
    def __init__(self, func):
        super(MyThread, self).__init__()
        self.func = func
    def run(self):
        self.func()

def downloader():
    global workQueue
    while not workQueue.empty():
        url, p = workQueue.get()
        print 'Downloading:', url
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        soup = BeautifulSoup(res.read())
        aImg =  soup.find(class_='commentlist').find_all('img')
        for img in aImg:
            #gif图片的org_src
            if img['src'][-3:] == 'gif':
                src = img['org_src']
            else:
                src = img['src']
            fName = str(p) + '-' + str(re.search(r'.+/(\w+.\w{3})', src).group(1))
            fPosition = os.path.join(SAVE_PATH, fName)
            if not os.path.exists(fPosition):
                urllib.urlretrieve(src, fPosition)
        workQueue.task_done()

def get_latest_page_num():
    #通过<a href="http://jandan.net/ooxx/page-1317#comments">1317</a>，找到最新的页码
    req = urllib2.Request('http://jandan.net/ooxx')
    res = urllib2.urlopen(req)
    html = res.read()
    soup = BeautifulSoup(html)
    page = soup.find(class_='current-comment-page').string
    page = re.search(r'(\d+)' , page).group()
    return int(page)

def main():
    global workQueue
    threads = []
    upperPage = get_latest_page_num()
    lowerPage = 1310  #页码下界

    for p in range(lowerPage, upperPage+1):
        url = 'http://jandan.net/ooxx/page-' + str(p)
        workQueue.put([url, p])

    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)

    for i in range(_THREAD_NUM):
        thread = MyThread(downloader)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    workQueue.join()
    print 'Downloading Successful!'

if __name__ == '__main__':
    main()