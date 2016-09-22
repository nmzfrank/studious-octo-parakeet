#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
import time

# browser = webdriver.Firefox()
# browser.get("http://baike.baidu.com/view/4608842.htm")
# time.sleep(10)
# browser.get("http://baike.baidu.com/view/1.htm")
# js = 'window.open("http://baike.baidu.com/view/1.htm");'
# browser.execute_script(js)
# handles = browser.window_handles
# for handle in handles:
# 	if(handle != browser.current_window_handle):
# 		browser.switch_to_window(handle)
# browser.close()


url = "http://tw.weibo.com/mason1/follow"
urls = []
urls.append(url)

if(isinstance(url, str)):
	print type(url)
if(isinstance(urls, list)):
	print type(urls)
