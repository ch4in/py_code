#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    下载煎蛋妹子图
    url: http://jandan.net/ooxx
    just4fun.
	example of image link:
	<img src="http://ww1.sinaimg.cn/mw600/8074970djw1eiqgynb3y4j20rs14s41z.jpg" style="max-width: 608px; max-height: 450px;">
"""

import sys, urllib, urllib2, time, re, os
from bs4 import BeautifulSoup

lowerbound_page = 1222  #页码下界
save_path = './img/'

def get_latest_page_num():
    #找到最新的页码
    req = urllib2.Request('http://jandan.net/ooxx')
    fd = urllib2.urlopen(req)
    html = fd.read()

    soup = BeautifulSoup(html)
    cur_page = soup.find(class_='current-comment-page').string
    cur_page = re.search(r'(\d+)' ,cur_page).group(0)
    return int(cur_page)

def download_img(p1, p2):
    #按页下载
    for p in range(p1, p2+1):
        url = 'http://jandan.net/ooxx/page-' + str(p)
        req = urllib2.Request(url)
        fd = urllib2.urlopen(req)
        html = fd.read()

        soup = BeautifulSoup(html)
        img_arr =  soup.find(class_='commentlist').find_all('img')

        #下载每一张图片
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        for img in img_arr:
            fname = str(p) + '-' + str(re.search(r'.+/(\w+.\w{3})', img['src']).group(1))
            f_position = os.path.join(save_path, fname)
            if not os.path.exists(f_position):
                urllib.urlretrieve(img['src'], f_position)


def main():
    num = get_latest_page_num()
    download_img(lowerbound_page, num)

if __name__ == '__main__':
    main()