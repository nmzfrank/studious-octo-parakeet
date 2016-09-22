#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
import threading
import time
import random


class get_and_search():
	"""docstring for get_and_search
	class for all webpage get and
	search function"""
	def __init__(self, urls, browser):
		self.urls = urls
		self.browser = browser

	def get(self):
		if(isinstance(self.urls, str)):
			self.getSinglePage()
		if(isinstance(self.urls, list)):
			self.getMultiplePages()

	def getSinglePage(self):
		self.browser.get(self.urls)
		all_content = self.browser.page_source
		self.search(all_content)
		self.preservePage(all_content.encode('utf-8'), self.urls)
		time.sleep(random.uniform(10, 40))

	def getMultiplePages(self):
		for url in self.urls:
			self.browser.get(url)
			all_content = self.browser.page_source
			self.search(all_content)
			self.preservePage(all_content.encode('utf-8'), url)
			time.sleep(random.uniform(10, 40))

	def preservePage(self, content, url):
		pass

	def searchConfig(self, param):
		pass

	def search(self, content):
		if(self.need_search == False):
			pass


class worker(threading.Thread):
	"""docstring for worker
	designed for completely parsing
	information of one user"""
	def __init__(self, uid, browser):
		threading.Thread.__init__()
		self.uid = uid

	def run(self):
		self.getUserProfile()
		self.getFollowee()
		self.getWeibo()
		