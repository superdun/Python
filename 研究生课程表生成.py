# -*- coding: utf-8 -*-
import xlrd
import xlwt
table = xlrd.open_workbook('123.xls').sheet_by_index(0)
course_name=[]
teacher_name=[]
classroom=[]
time=[]
week=[]
file=xlwt.Workbook()
new_table=file.add_sheet('hahaha!! by Dun')
new_table.write(0,1,u'周一')
new_table.write(0,2,u'周二')
new_table.write(0,3,u'周三')
new_table.write(0,4,u'周四')
new_table.write(0,5,u'周五')
new_table.write(0,6,u'周六')
new_table.write(0,7,u'周日')
new_table.write(1,0,u'第一节')
new_table.write(2,0,u'第二节')
new_table.write(3,0,u'第三节')
new_table.write(4,0,u'第四节')
new_table.write(5,0,u'第五节')
for i in range(2,table.nrows-3):
    course_name.append(table.row_values(i)[4])
    teacher_name.append(table.row_values(i)[6])
    classroom.append(table.row_values(i)[9])
    time.append(table.row_values(i)[8])
    week.append(table.row_values(i)[7])
    if '/' in table.row_values(i)[10]:
        course_name.append(table.row_values(i)[4])
        teacher_name.append(table.row_values(i)[6])
        classroom.append(table.row_values(i)[11])
        time.append(table.row_values(i)[10])
        week.append(table.row_values(i)[7])
    if '/' in table.row_values(i)[12]:
        course_name.append(table.row_values(i)[4])
        teacher_name.append(table.row_values(i)[6])
        classroom.append(table.row_values(i)[13])
        time.append(table.row_values(i)[12])
        week.append(table.row_values(i)[7])

def locate(x):
    locx=0
    locy=0
    inner=''
    if time[x][1]==u'一':
        locx=1
    elif time[x][1]==u'二':
        locx=2
    elif time[x][1]==u'三':
        locx=3
    elif time[x][1]==u'四':
        locx=4
    elif time[x][1]==u'五':
        locx=5
    elif time[x][1]==u'六':
        locx=6
    else:
        locx=7
    if time[x][3]=='1':
        locy=1
    elif time[x][3]=='3':
        locy=2
    elif time[x][3]=='5':
        locy=3
    elif time[x][3]=='7':
        locy=4
    elif time[x][3]=='9':
        locy=5
    print course_name[x]
    print teacher_name[x]
    print classroom[x]
    print time[x]
    print week[x]
    inner=course_name[x]+'\n '+teacher_name[x]+'\n '+classroom[x]+'\n '
    write(locx,locy,inner)
def write(x,y,inner):
    try:
         new_table.write(y,x,inner)
         new_table.col(x).width=6000
    except:
         pass
    finally:
         pass

def main():
    for i in range(len(course_name)):
        locate(i)
    file.save('new_kcb.xls')
if __name__=='__main__':
    main()