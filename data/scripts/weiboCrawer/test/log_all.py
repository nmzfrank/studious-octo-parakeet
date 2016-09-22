#!usr/bin/python
# -*- coding: UTF-8 -*-
import time


def except_info(content):
	time_stamp = time.strftime("%H:%m:%S\t")
	buff = time_stamp + content
	print buff


def result_save(content):
	print content


def error_log(content):
	filename = time.strftime("%Y-%m-%d %H:%M:%S-log.txt", time.localtime(time.time()))
	log = open(filename, 'w')
	log.write(content)


if __name__ == '__main__':
	error_log("test")
