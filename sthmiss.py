f1 = open("xgb.csv")
f2 = open("t.csv")
line1 = f1.readline()
line2 = f2.readline()
lines = []
while line2:
    lines.append(line2)
    line2 = f2.readline()
count = 0
while line1:
    if line1 not in lines:
        print line1  
        count += 1
    line1 = f1.readline()
print count
