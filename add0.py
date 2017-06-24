fin = open("test.csv")
fout = open("testout.csv","w")
line = fin.readline()[:-1]
while line:
    while len(line) < 10:
        line = '0'+line
    fout.write(line+'\n')
    line = fin.readline()[:-1]
