# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
import cv2
import numpy as np
def pic_job():
    image = Image.open('aaa.jpg')
    new_size = (int(image.size[0]*200/image.size[1]),200)
    image_resized = image.resize(new_size, Image.ANTIALIAS)
    image_resized.save('beauty.jpg', 'jpeg')
def check_face(img):
    global num_face
    single_face=[]
    area=0
    face=face_cascade.detectMultiScale(img, scaleFactor=1.03, minNeighbors=5)
    num_face=len(face)
    if len(face)==1:
        return face
    elif len (face)==0:
        print 'error! no face checked!'
    else:
        for i in range(len(face)):
            if face[i][2]*face[i][3]>area:
                area=face[i][2]*face[i][3]
                single_face.append(face[i])
            else:
                pass
        return single_face
def check_eyes(range_g,range_c):
    global num_eyes
    global lex,ley,lew,leh,rew,reh,rex,rey
    eyes = eye_cascade.detectMultiScale(range_g)
    num_eyes=len(eyes)
    area1=0
    area2=0
    print str(len(eyes))+'eyes'
    if len(eyes)==2:
        if eyes[0][0]<eyes[1][0]:
            lex=eyes[0][0]
            ley=eyes[0][1]
            lew=eyes[0][2]
            leh=eyes[0][3]
            rex=eyes[1][0]
            rey=eyes[1][1]
            rew=eyes[1][2]
            reh=eyes[1][3]
        else:
            lex=eyes[1][0]
            ley=eyes[1][1]
            lew=eyes[1][2]
            leh=eyes[1][3]
            rex=eyes[0][0]
            rey=eyes[0][1]
            rew=eyes[0][2]
            reh=eyes[0][3]
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(range_c,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    elif len(eyes)==1:
        if eyes[0][0]<w/2:
            lex=eyes[0][0]
            ley=eyes[0][1]
            lew=eyes[0][2]
            leh=eyes[0][3]
            rex=w-(lex+lew) #eyes' x,y is relative to face not to the pic
            rey=ley
            rew=lew
            reh=leh
        else:
            rex=eyes[0][0]
            rey=eyes[0][1]
            rew=eyes[0][2]
            reh=eyes[0][3]
            lex=w-(rex+rew)
            ley=rey
            lew=rew
            leh=reh
        cv2.rectangle(range_c,(lex,ley),(lex+lew,ley+leh),(0,255,0),2)
        cv2.rectangle(range_c,(rex,rey),(rex+rew,rey+reh),(0,255,0),2)
    elif len(eyes)>2:
        for i in range(len(eyes)):
            if eyes[i][0]<=w/2:
                if eyes[i][2]*eyes[i][3]>area1 and eyes[i][1]<h/2:
                    area1=eyes[i][2]*eyes[i][3]
                    lex=eyes[i][0]
                    ley=eyes[i][1]
                    lew=eyes[i][2]
                    leh=eyes[i][3]
                else:
                    pass
            else:
                if eyes[i][2]*eyes[i][3]>area2 and eyes[i][1]<h/2:
                    area2=eyes[i][2]*eyes[i][3]
                    rex=eyes[i][0]
                    rey=eyes[i][1]
                    rew=eyes[i][2]
                    reh=eyes[i][3]
                else:
                    pass
        cv2.rectangle(range_c,(lex,ley),(lex+lew,ley+leh),(0,255,0),2)
        cv2.rectangle(range_c,(rex,rey),(rex+rew,rey+reh),(0,255,0),2)
    else:
        print "error!no eyes!"
def check_mouth(range_g,range_c):
    global mx,my,mh,mw,num_mouth
    area=0
    mouth=mouth_cascade.detectMultiScale(range_g)
    num_mouth=len(mouth)
    print str(len(mouth))+'mouths'
    if len(mouth)==0:
        print 'no mouth'
    elif len(mouth)==1:
        mx=mouth[0][0]
        my=mouth[0][1]
        mh=mouth[0][3]
        mw=mouth[0][2]
        cv2.rectangle(range_c,(mx,my),(mx+mw,my+mh),(31,123,123),2)
    else:	 
        for (t_mx,t_my,t_mw,t_mh) in mouth:
            if t_mw*t_mh>area and t_my>ny:
                area=t_mw*t_mh
                mx=t_mx
                my=t_my
                mh=t_mh
                mw=t_mw
            else:
                pass	
        cv2.rectangle(range_c,(mx,my),(mx+mw,my+mh),(31,123,123),2)
def check_smile(range_g,range_c):
    global num_smile
    smile=smile_cascade.detectMultiScale(range_g)
    num_smile=len(smile)
    for (sx,sy,sw,sh) in smile:
        cv2.rectangle(range_c,(sx,sy),(sx+sw,sy+sh),(0,45,32),2)
def check_nose(range_g,range_c):
    global nx,ny,nw,nh
    area=0
    nose=nose_cascade.detectMultiScale(range_g)
    print str(len(nose))+'noses'
    if len(nose)==0:
        print 'no nose'
    elif len(nose)==1:
        nx=nose[0][0]
        ny=nose[0][1]
        nh=nose[0][3]
        nw=nose[0][2]
        cv2.rectangle(range_c,(nx,ny),(nx+nw,ny+nh),(31,123,23),2)
    else:	 
        for (t_nx,t_ny,t_nw,t_nh) in nose:
            if t_nw*t_nh>area and t_ny>ley:
                area=t_nw*t_nh
                nx=t_nx
                ny=t_ny
                nh=t_nh
                nw=t_nw
            else:
                pass	
        cv2.rectangle(range_c,(nx,ny),(nx+nw,ny+nh),(31,123,23),2)	
def state(gap):
    if gap<=0.01:
        return 10
    elif gap<=0.05:
        return 9
    elif gap<=0.1:
        return 7
    elif gap<=0.5:
        return 6
    elif gap<1:
        return 4
    elif gap<2:
        return 3
    else:
        return 1
def score():
    global x,y,w,h,nx,ny,nw,nh,lex,ley,leh,lew,rex,rey,reh,rew,sx,sy,sw,sh,mx,my,mh,mw
    if lew*leh<rew*reh:
	    eye_area=lew*leh*2
    else:
        eye_area=rew*reh*2
    proportion_score=state(abs(w/h-1.0))+state(abs(w/lew-4.2368))+state(abs(w/rew-4.4722))+state(abs(h/leh-4.2368))+state(abs(h/reh-4.2722))+state(abs(w/nw-4.1282))+state(abs(h/nh-5.0313))+state(abs(w/nw-2.9815))+state(abs(h/mh-5.0313))
    location_score=state(abs(lex/w-0.1925))+state(abs(rex/w-0.5590))+state(abs(ley/h-0.2795))+state(abs(rey/h-0.2795))+state(abs(mx/w-0.3416))+state(abs(my/h-0.7143))+state(abs(nx/w-0.3727))+state(abs(ny/h-0.5217))+state(abs(nw/mw-0.1925))
    area_score=220*(eye_area)/(w*h)+state(abs(w*h/(nh*nw)-20.7700))-100*(mh*mw)/(w*h)
    score=proportion_score/60*25+location_score/80*25+area_score/30*50  
    print 	proportion_score,location_score,area_score
    print '你的颜值为：'.decode('utf-8','ignore').encode('GBK','ignore'),int(score),'分！'.decode('utf-8','ignore').encode('GBK','ignore')

pic_job()
x=y=w=h=nx=ny=nw=nh=lex=ley=leh=lew=rex=rey=reh=rew=sx=sy=sw=sh=mx=my=mh=mw=0.1
num_face=num_eyes=num_mouth=num_nose=num_smile=0  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
mouth_cascade=cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
nose_cascade=cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
img = cv2.imread('beauty.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face=check_face(gray_img)
x=face[0][0]
y=face[0][1]
w=face[0][2]
h=face[0][3]

cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
roi_gray = gray_img[y:y+h, x:x+w]
roi_color = img[y:y+h, x:x+w]
check_eyes(roi_gray,roi_color)
check_nose(roi_gray,roi_color)
check_mouth(roi_gray,roi_color)
#check_smile(roi_gray,roi_color)
print '!!!',w/h, w/lew,w/rew,h/leh,h/reh,w*h/(lew*leh+rew*reh),w/nw,h/nh,w/mw,h/mh,w*h/(nh*nw),w*h/(mh*mw)
print '!!!!',lex/w,rex/w,ley/h,rey/h,mx/w,my/h,nx/w,ny/h,nw/mw
score()
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()