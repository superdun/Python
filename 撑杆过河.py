import cv2
import video
import sys
import serial
import time
seed_pt=[2,2]
def onmouse(event, x, y, flags, param):
	global seed_pt
	if flags & cv2.EVENT_FLAG_LBUTTON:
		seed_pt = x, y
		time.sleep(1)
		serial_com('touch')
def main_check(vis,gray,seed_pt):
	
	cv2.circle(vis,(seed_pt[0],seed_pt[1]), 5, (0,0,255), -1)
	check_edge(vis,gray,'b','l',seed_pt)
	left_pos=result
	check_edge(vis,gray,'b','r',seed_pt)
	right_pos=result
	check_edge(vis,gray,'w','u',[left_pos[0]-1,left_pos[1]])
	left_up_pos=result
	check_edge(vis,gray,'w','u',[right_pos[0]+1,right_pos[1]])
	right_up_pos=result
	base_alt=(left_up_pos[1]+right_up_pos[1])/2
	width=right_up_pos[0]-left_up_pos[0]
	cv2.line(vis,(left_up_pos[0]-1,base_alt-width-5),(right_up_pos[0]-1,base_alt-width-5),(255,0,0))
	if width<41:
		time.sleep(0.5)
		
		serial_com('stop')
	else:
		for i in range(20):
			if gray[base_alt-width+48][left_up_pos[0]+i-5]<20 :#change here if ping is not good
				serial_com('stop')
				cv2.line(vis,(left_up_pos[0]-1,base_alt-width-5),(right_up_pos[0]-1,base_alt-width-5),(25,98,0))
				if seed_pt[0]!=2:
					time.sleep(3)
					serial_com('touch')

				break
def main():
	try:
		fn = sys.argv[1]
	except:
		fn = 0
	cv2.namedWindow('edge')

	cap = video.create_capture(fn)
	cv2.setMouseCallback('edge', onmouse)
	global ser
	ser = serial.Serial('COM4',9600)
	count =0
	while True:
		#print seed_pt[0]
		flag, img = cap.read()
		vis=img.copy()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		if count%2==0:
			main_check(vis,gray,seed_pt)
				
		cv2.imshow('edge', vis)
		count+=1
		ch = cv2.waitKey(5) & 0xFF
		if ch == 27:
			break
		
def check_edge(img,gray_img,color,direct,pos):
	i=0
	j=0
	global result
	result=[1,1]

	if color=='b':
		while True:
			if gray_img[pos[1]-j][pos[0]-i]<20:
				cv2.circle(img,(pos[0]-i,pos[1]-j), 5, (230,123,255), -1)
				result=[pos[0]-i,pos[1]-j]
				break
			elif direct=='l' and pos[0]-i>0 and pos[0]-i<639 and pos[1]-j>0 and pos[1]-j<359:
				i+=1
			elif direct=='r' and pos[0]-i>0 and pos[0]-i<639 and pos[1]-j>0 and pos[1]-j<359:
				i-=1
			elif direct=='u' and pos[0]-i>0 and pos[0]-i<639 and pos[1]-j>0 and pos[1]-j<359:
				j+=1
			else:
				break
	if color=='w':
		while True:
			if gray_img[pos[1]-j][pos[0]-i]>50:
				cv2.circle(img,(pos[0]-i,pos[1]-j), 5, (23,123,255), -1)
				result=[pos[0]-i,pos[1]-j]
				break
			elif direct=='l' and pos[0]-i>0 and pos[0]-i<639 and pos[1]-j>0 and pos[1]-j<359:
				i+=1
			elif direct=='r' and pos[0]-i>0 and pos[0]-i<639 and pos[1]-j>0 and pos[1]-j<359:
				i-=1
			elif direct=='u' and pos[0]-i>0 and pos[0]-i<639 and pos[1]-j>0 and pos[1]-j<359:
				j+=1
			else:
				break			
def serial_com(style):
	if style=='touch':
		ser.write('a')
	elif style=='stop':
		ser.write('b')
	else:
		ser.write('c')
	print style

if __name__ == '__main__':
	main()
