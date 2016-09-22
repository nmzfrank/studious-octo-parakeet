#!usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
from selenium import webdriver
import log_all


class spider(threading.Thread):
    """docstring for spider"""

    def __init__(self, browser, urls, selector, semaphore):
        threading.Thread.__init__(self)
        self.browser = browser
        self.urls = urls
        self.selector = selector
        self.semaphore = semaphore

    def run(self):
        self.semaphore.acquire()
        while(len(self.urls) > 0):
            url = self.urls.pop()
            self.semaphore.release()
            self.browser.open(url)
            try:
                element = self.browser.find_element_by_css_selector(self.selector)
            except:
                log_all.except_info("unable to find " + self.selector + " @page " + self.url)
            else:
                log_all.result_save(element.text)
            time.sleep(30)
            self.browser.close()
            self.semaphore.acquire()
        self.semaphore.release()


class parsePages():
    """intend to parse a specific dom element on a series of web pages"""

    def __init__(self, proxies, url_pre, url_post, start, end, selector):
        self.proxies = proxies
        self.url_pre = url_pre
        self.url_post = url_post
        self.start = start
        self.end = end
        self.selector = selector

    def setProxy(self, browser, proxy):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.update_preferences()
        return profile

    def getPages(self):
        target_url_list = []
        semaphore = threading.Semaphore(10)
        for i in range(self.start, self.end + 1, 1):
            target_url_list.append(self.url_pre + str(i) + self.url_post)
        for i in range(20):
            spider(webdriver.Firefox(), target_url_list, self.selector, semaphore)
