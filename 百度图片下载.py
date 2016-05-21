# -*- coding: utf-8 -*-
import requests
import json
import sys
import re
import urllib
import os
import socket
class start(object):
	def __init__(self):
		self.uncode_name=raw_input('请输入要搜索的关键词！>>>'.decode('utf-8','ignore').encode('GBK'))
		self.name=urllib.quote((self.uncode_name).decode(sys.stdin.encoding).encode('utf-8'))
		self.num=raw_input('请输入抓取图片数量>>>'.decode('utf-8','ignore').encode('GBK'))
		self.net_ctr()
	def net_ctr(self):
		headers= {'Accept':'image/webp',
		'User-Agent':'''Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6''',}
		goal_url='http://image.baidu.com/i?tn=resultjson_com&ie=utf-8&pn=0&word=%s&rn=%s&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1#'%(self.name,self.num)
		print goal_url
		r=requests.get(goal_url,headers=headers,timeout=100)
		self.content=r.content
		self.res()
	def res(self):
		comp= re.compile(r'\"objURL\":\"(.*?)\",',re.S)
		result= comp.findall(self.content)
		self.result_url=[]
		for i in result:
			self.result_url.append(self.enco(i))
		download(self.result_url,self.uncode_name,self.num)
	def enco(self,s):
		dic = {
		"0": "7",   "1": "d",   "2": "g",   "3": "j",   "4": "m",   "5": "o",   "6": "r",   "7": "u",   "8": "1",
		"9": "4",   "a": "0",   "b": "8",   "c": "5",   "d": "2",   "e": "v",   "f": "s",   "g": "n",   "h": "k",
		"i": "h",   "j": "e",   "k": "b",   "l": "9",   "m": "6",   "n": "3",   "o": "w",   "p": "t",   "q": "q",
		"r": "p",   "s": "l",   "t": "i",   "u": "f",   "v": "c",   "w": "a"
		}
		s = s.replace("AzdH3F","/")
		s = s.replace("_z2C$q",":")
		s = s.replace("_z&e3B",".")
		p=''
		for i in s:
			if i in dic.keys():
				p += dic[i]
			else:
				p += i
		return p
def download(urllist,dir_name,dir_len):
	print '地址解析完毕，下载中........'.decode('utf-8','ignore').encode('GBK')
	os.mkdir(dir_name)
	for i in range(len(urllist)):
		try:
			img_name=dir_name+'\\'+dir_name+'__'+str(i+1)+'.jpg'
			print img_name+' done!'
			socket.setdefaulttimeout(10)
			urllib.urlretrieve(urllist[i],img_name)
		except:
			print 'EROR!'
		finally:
			pass
ok=start()