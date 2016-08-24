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
        else:
            print elem.text
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


if __name__ == '__main__':
    urls = []
    for i in range(10):
        url = "http://baike.baidu.com/view/" + str(i) + ".htm"
        urls.append(url)
    patchParsing(urls)
