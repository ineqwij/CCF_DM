import matplotlib.pyplot as plt
import numpy as np
import random
f = open('data.csv')
count = 0
line = f.readline()

def bad_date2good_date(bad_date):
    s = bad_date.split('/');
    if s[1]=='1':
        good_date = int(s[2])
    elif s[1]=='2':
        good_date = int(s[2])+31
    elif s[1]=='3':
        good_date = int(s[2])+59
    elif s[1]=='4':
        good_date = int(s[2])+90
    elif s[1]=='5':
        good_date = int(s[2])+120
    elif s[1]=='6':
        good_date = int(s[2])+151
    elif s[1]=='7':
        good_date = int(s[2])+181
    elif s[1]=='8':
        good_date = int(s[2])+212
    elif s[1]=='9':
        good_date = int(s[2])+243
    elif s[1]=='10':
        good_date = int(s[2])+273
    elif s[1]=='11':
        good_date = int(s[2])+304
    elif s[1]=='12':
        good_date = int(s[2])+334
    
    return good_date
    

def sort_by_date(tables):
    table = []
    for i in range(365):
        table.append(0)
    for i in range(len(tables)):
        if tables[i][4]!='':
            table[ bad_date2good_date(tables[i][1])-1 ]= float(tables[i][4])
        else:
            table[ bad_date2good_date(tables[i][1])-1 ]= float(10)
    return table

def RA1():
    fx = open('D:/CCF_DM/data/train.csv')
    tnum = random.randint(1, 1415)
    countx = 0
    while countx != tnum:
        linex = fx.readline()
        countx += 1
    sx = linex[:-1].split(',')
    return sx[0]

def RA2():
    fx = open('D:/CCF_DM/data/train.csv')
    tnum = random.randint(1416, 10037)
    linex = fx.readline()
    countx = 1
    while countx != tnum:
        linex = fx.readline()
        countx += 1
    sx = linex[:-1].split(',')
    return sx[0]

# No1 = raw_input("please input the number")
No1 = RA1()
print No1
No_table1=[]
# No2 = raw_input("please input the number")
No2 = RA2()
No_table2=[]
print No2

while line:
    if count==6314494:
        break
    count+=1
    line = f.readline()
    line = line[:-2]
    s = line.split(',')
    for i in range(5):
        s[i] = s[i][1:-1]
    if s[0] == No1:
        No_table1.append(s)
    elif s[0] == No2:
        No_table2.append(s)
     
y1 =sort_by_date(No_table1)
y2 =sort_by_date(No_table2)
print y1
print y2
x = np.arange(1, 366, 1)
plt.plot(x, y1, color = 'red')
plt.plot(x, y2, color = 'blue')
plt.show()

