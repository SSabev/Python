f = open('tbcities.dat', 'r')

temp = []

for line in f:
    temp.append([t.rstrip() for t in line.split('\t')])

f.close()

w = open('tbcities.sql', 'w')

for i in temp:
    w.write("INSERT INTO CITIES VALUES ('%s', '%s', %s, %s);\n"%(i[0], i[1], i[2], i[3]))

w.close()
