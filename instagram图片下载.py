# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq 
import os
import sys
import socket
import urllib
import datetime
import lxml.etree
import lxml._elementpath
import gzip
now = datetime.datetime.now()
data=now.strftime('%Y-%m-%d')
time=now.strftime('%Y-%m-%d %H:%M:%S')
class network(object):
	def __init__(self):
		self.openurl='http://pinsta.me/figarotseng'
		self.next_web_url=''
		self.img_url=[]
		self.img_desc=[]
	def get_web(self):
		self.web=requests.get(self.openurl+self.next_web_url,timeout=10)
		print self.openurl+self.next_web_url
		self.d=pq(self.web.content)
		self.next_web_url=self.d('.nextPage').attr('href')
	def get_imgs_url(self):
		for i in self.d('.image'):
			if start.count <start.num:
				self.img_url.append(self.d(i).attr('srcx'))
				self.img_desc.append(self.d(i).parents('.brickBody').find('.caption').text())
				start.count+=1
			else:
				break
	def get_imgs_url_fresh(self):
		last_img_url=open('record.txt','r').read()
		print last_img_url
		for i in self.d('.image'):
			print self.d(i).attr('srcx')!=last_img_url
			if self.d(i).attr('srcx')!=last_img_url:
				self.img_url.append(self.d(i).attr('srcx'))
				self.img_desc.append(self.d(i).parents('.brickBody').find('.caption').text())
				start.freshcount+=1
			else:
				start.ifnextpage=2
				break
network=network()	
def docs(urls,descrep):
	try:
		os.mkdir('曾少宗__pic'.decode('utf-8','ignore').encode('GBK','ignore'))
	except:
		pass
	finally:
		pass
	print urls
	open('url.txt','w').write(str(urls))
	for i in range(len(urls)):
		try:
			print 'ok a pic!'
			socket.setdefaulttimeout(60)
			urllib.urlretrieve(urls[i],'曾少宗__pic'.decode('utf-8','ignore').encode('GBK','ignore')+'\\%s_%s_%d.%s'%(data,descrep[i],i,urls[i][-3:]))
		except:
			print 'ERROR'
		finally:
			pass
	if len(urls)>0:
		open('record.txt','w').write(urls[0])
	else:
		pass
class start(object):
	def __init__(self):
		self.style=raw_input('更新请输入1，新下载请输入2\n>>>>>>'.decode('utf-8','ignore').encode('GBK'))
		if self.style=='2':
			self.num=int(raw_input('请输入下载数量\n>>>>>>'.decode('utf-8','ignore').encode('GBK')))
		else:
			pass
		self.count=0
		self.freshcount=0
		self.ifnextpage=1
	def do_it(self):
		if self.style=='2':
			while self.count <self.num:
				network.get_web()
				network.get_imgs_url()
			docs(network.img_url,network.img_desc)
		elif self.style=='1':
			while self.ifnextpage==1:
				network.get_web()
				network.get_imgs_url_fresh()
			print 'refresh %d pics'%len((network.img_url))
			docs(network.img_url,network.img_desc)
start=start()
start.do_it()	
		