#!usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
from selenium import webdriver


class Spider(threading.Thread):
    def __init__(self, url, browser, threadLock):
        threading.Thread.__init__(self)
        self.url = url
        self.browser = browser
        self.threadLock = threadLock

    def run(self):
        js = 'window.open("' + self.url + '");'
        self.threadLock.acquire()
        self.browser.execute_script(js)
        self.threadLock.release()
        time.sleep(30)
        self.threadLock.acquire()
        try:
            elem = self.browser.find_element_by_css_selector("h1")
        except:
            print "unable to find h1 element"
        print elem.text
        





def patchParsing(urls):
    browser = webdriver.Firefox()
    browser.get("http://baike.baidu.com/view/1136308.htm")
    threadLock = threading.Lock()
    for url in urls:
        Spider(url,browser,threadLock)
        Spider.start()
