#!usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time
from selenium import webdriver


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print threadName + ":" + time.ctime(time.time())


def open_browser(browser, lock, url):
    js = 'window.open("' + url + '");'
    lock.acquire()
    browser.execute_script(js)
    lock.release()
    time.sleep(30)
    lock.acquire()
    elem = browser.find_element_by_css_selector("h1")
    print elem.text
    browser.close()
    handles = browser.window_handles
    browser.switch_to_window(handles[0])
    lock.release()


browser = webdriver.Firefox()
# browser.implicitly_wait(10)
# browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')
browser.get('http://baike.baidu.com/view/1136308.htm')
lock = thread.allocate_lock()

try:
    thread.start_new_thread(open_browser, (browser, lock, "http://baike.baidu.com/view/1.htm"))
    thread.start_new_thread(open_browser, (browser, lock, "http://baike.baidu.com/view/2.htm"))
except:
    print "Error: unable to start thread"
time.sleep(30)
lock.acquire()
elem = browser.find_element_by_css_selector("h1")
print elem.text
browser.close()
handles = browser.window_handles
browser.switch_to_window(handles[0])
lock.release()

while 1:
    pass
