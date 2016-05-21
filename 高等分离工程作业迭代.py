# -*- coding: utf-8 -*-
#Homework of Separation engineering 
#code by Dun 2015-09-23
import math
def print_data():
    #Show the known conditions
    print '已知Ki=Ci*exp[-Ei/(1.8*t+492)]'.decode('utf-8','ignore').encode('GBK','ignore')
    print'''
    __________________________________
    组分      Ci       Ei        Xi
    ----------------------------------
     1       4E3/P    4.6447E3    1/3
     2       8E3/P    4.6447E3    1/3
     3      12E3/P    4.6447E3    1/3
    __________________________________
    '''.decode('utf-8','ignore').encode('GBK','ignore')
	#input the initial temperature
    return raw_input('请输入第一次试差温度（无符号） ，退出请ctrl+c  >>>'.decode('utf-8','ignore').encode('GBK','ignore'))
#define some function for calculating
def calculate_K(C,E,t):
    return C*math.exp(-E/(1.8*t+492))

def calculate_fi(K,x):
    return K*x

def calculate_fi_d(fi,E,t):
    return fi*E/pow(1.8*t+492,2)
# The main function
def run_interation(x):
    precision=raw_input('请输入精确度（如0.0001）  >>>'.decode('utf-8','ignore').encode('GBK','ignore'))
    t_init=float(x)
    count=1
    E=[4644.7,4644.7,4644.7]
    x=[1/3.0,1/3.0,1/3.0]
    C=[4000,8000,12000]
    while True:
        K=[]
        fi=[]
        fi_d=[]
        for i in range(3):
            K.append(calculate_K(C[i],E[i],t_init))
            print calculate_K(C[i],E[i],t_init)
            fi.append(calculate_fi(K[i],x[i]))
            fi_d.append(calculate_fi_d(fi[i],E[i],t_init))
        fi_total=fi[0]+fi[1]+fi[2]
        fi_d_total=fi_d[0]+fi_d[1]+fi_d[2]
        print'第%d次试差，假定t=%f'.decode('utf-8','ignore').encode('GBK','ignore')%(count,t_init)
        print '''
    __________________________________________________________________
    组分           Ki          Ki*xi            Ki*xi*Ei/(1.8*t+492)^2
    ------------------------------------------------------------------
     1       %f         %f                %f
     2       %f         %f                %f
     3       %f         %f                %f
	                      %f                %f
    __________________________________________________________________
        '''.decode('utf-8','ignore').encode('GBK','ignore')	%(K[0],fi[0],fi_d[0],K[1],fi[1],fi_d[1],K[2],fi[2],fi_d[2],fi_total,fi_d_total)
        print 'f(%f)=%f'%(t_init,fi_total-1)
        print 'f(%f)=%f'%(t_init,fi_d_total*1.8)
        if abs(fi_total-1)<=float(precision):
            break
        else:
            count+=1
            print '不满足目标函数，准备开始下一次迭代.....'.decode('utf-8','ignore').encode('GBK','ignore')
            print 't_init=%f-%f'%(t_init,(fi_total-1)/(fi_d_total*1.8))
            t_init=t_init-(fi_total-1)/(fi_d_total*1.8)
    print_result(t_init)
def print_result(result):
    print '##################################'
    print '求得泡点温度 t=%f'.decode('utf-8','ignore').encode('GBK','ignore')%result
    print '##################################'

run_interation(print_data())