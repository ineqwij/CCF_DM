import matplotlib.pyplot as plt
import numpy as np
import random as rdm
f = open('D:/CCF_DM/data/train.csv')
line = f.readline()
count = 0
ID0 = []
ID1 = []
n1 = 1
n0 = 1
R0 = []
R1 = []
i = 0
while i < 1000:
    tempN1 = rdm.randint(1,1415)
    if tempN1 in R1:
        continue
    else:
        R1.append(tempN1)
        i += 1
i = 0
while i < 1000:
    tempN0 = rdm.randint(1,8622)
    if tempN0 in R0:
        continue
    else:
        R0.append(tempN0)
        i += 1
while line:
    line = line[:-1]
    s = line.split(',')
    # print s
    if s[1] == '0':
        idt = s[0][-3:]
        if n0 in R0:
            ID0.append(idt)
        n0 += 1
    if s[1] == '1':
        idt = s[0][-3:]
        if n1 in R1:
            ID1.append(idt)
        n1 += 1
    line = f.readline()
x0 = np.arange(1, 1001, 1)
x1 = np.arange(1, 1001, 1)
plt.scatter(x1, ID1, color = 'red')
plt.scatter(x0, ID0, color = 'blue')
plt.show()
# 1415--'1'
# 8622--'0'
# 10037
