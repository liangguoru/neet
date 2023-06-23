#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import threading
# from common.retry_func import retry_fun

# @retry_fun(retries=3, timeout_second=3)
def handle_html_for_django(inputfile = 'bak-gallery2.html'):
	motomoto = []
	with open(inputfile,'r') as fd:
		for line in fd.readlines():
			motomoto.append(line)
	with open('gallery2.html','w') as fd:
		def chanege_line(line):
			#print (line)
			pos1 = line.find('"')
			spos = pos1 + 1
			pos2 = line.find('"',spos)
			frontline = line[:pos1]
			backline = line[pos2+1:]
			midline = line[pos1+1:pos2]
			newline = frontline+ '"{%' +" static '" +midline+ "' %}" + '"' +backline
			return newline
		for line in motomoto:
			if '"assets' in line:
				fd.write(chanege_line(line))
			else:
				fd.write(line)
				

if __name__ == '__main__':
    handle_html_for_django()
   
