#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    下载煎蛋妹子图
    url: http://jandan.net/ooxx
    just4fun.
	example of image link:
	<img src="http://ww1.sinaimg.cn/mw600/8074970djw1eiqgynb3y4j20rs14s41z.jpg" style="max-width: 608px; max-height: 450px;">
"""

import sys, urllib, time, re, os

def download_img(page):
    html = urllib.urlopen('http://jandan.net/ooxx/page-' + str(page))
    pattern = re.compile(r'http://ww\d{1}.sinaimg.cn/mw600/(.+?\.\w+)')
    
    imgs = re.findall(pattern, html.read())
    html.close()
    if(not os.path.exists('./imgs')):
        os.mkdir('./imgs')
    for img in imgs:
        if not os.path.exists('./imgs/' + img):
            download_url = 'http://ww1.sinaimg.cn/mw600/' + img
            urllib.urlretrieve(download_url, './imgs/%s' % img)
            print img

if __name__ == '__main__':
    try:
        b = int(sys.argv[1])
        if len(sys.argv) == 3:
            e = int(sys.argv[2])
        else:
            e = b
        for page in range(b, e+1):
            download_img(page)
    except ValueError,e:
        print u'输入开始页码和结束页码，已空格分开。'