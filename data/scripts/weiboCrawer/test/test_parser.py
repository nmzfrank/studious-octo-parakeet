#!usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
from selenium import webdriver
import chardet


class Spider(threading.Thread):

    def __init__(self, url, browser, threadLock, selector="h1"):
        threading.Thread.__init__(self)
        self.url = url
        self.browser = browser
        self.threadLock = threadLock
        self.selector = selector

    def run(self):
        filename = self.url.split('/')[-1].split('.')[0] + ".txt"
        file = open(filename, 'w')
        js = 'window.open("' + self.url + '");'
        self.threadLock.acquire()
        self.browser.execute_script(js)
        self.threadLock.release()
        time.sleep(30)
        self.threadLock.acquire()
        try:
            elem = self.browser.find_element_by_css_selector(self.selector)
        except:
            print "unable to find " + self.selector + " element"
        else:
            print elem.text
        file.write(self.browser.page_source.encode('utf-8'))
        self.browser.close()
        handles = self.browser.window_handles
        self.browser.switch_to_window(handles[0])
        self.threadLock.release()


def patchParsing(urls):
    browser = webdriver.Firefox()
    browser.get("http://baike.baidu.com/view/1136308.htm")
    threadLock = threading.Lock()
    for url in urls:
        Spider(url, browser, threadLock).start()


def get_10_pages(urls, selector="h1"):
    browser = webdriver.Firefox()
    browser.get("http://www.baidu.com")
    threadLock = threading.Lock()
    threadList = []
    for url in urls:
        spider = Spider(url, browser, threadLock, selector)
        threadList.append(spider)
        spider.start()
    for spider in threadList:
        spider.join()
    try:
        elem = browser.find_element_by_css_selector(selector)
    except:
        print "unable to find " + selector + " element"
    else:
        print elem.text
    browser.close()


if __name__ == '__main__':
    urls = []
    for i in range(1):
        url = "http://baike.baidu.com/view/" + str(i) + ".htm"
        urls.append(url)
    # get_10_pages(urls)
    patchParsing(urls)
