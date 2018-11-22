# ftp = ftplib.FTP('172.16.6.15', 'ftp', 'admin')
# ftp.cwd('/RPM416/2018/NOV/20')
# print(ftp.dir())
# f = open('d:\\rpm.dat', 'wb')
# ftp.makepasv()
# ftp.retrbinary('RETR' + ' FILE0001.RDF', f.write)
# ftp.close()
# f.close()

# x = 0x49177981
    # print(" hex= {0:02x} dec= {0:02}".format(x) + " float= ", end=" ");
    # print(x);
    # try:
    #     print(datetime.utcfromtimestamp(x+1514764800-1199232000))   # +10 years
    # except:
    #     print()

#Начало:         start=0x68
#1-я строчка:    x = byte[start+7] + byte[start+6] + byte[start+5] + byte[start+4]
#               ch12 = byte[start+8]; ch13 = byte[start+12]; ch14 = byte[start+16]; ch15 = byte[start+20]
#
#2-я строчка: start = start + 88

start = 0x68
delta = 0x58
count = 21
base4 = 0x1000000
base3 = 0x10000
base2 = 0x100
ifile = open('d:\\rpm21.dat', 'rb')
ofile = open('d:\\rpm21.csv', 'w')
ifile.seek(start)
data = ifile.read(count)
while data:
    x = hex(data[7] * base4 + data[6] * base3 + data[5] * base2 + data[4])
    # print(x)
    x = int(x, 16) + 1514764800 - 1199232000  # + 10лет - 2 часа
    dt = datetime.utcfromtimestamp(x)
    # print(dt)
    date, time = str(dt).split()[0], str(dt).split()[1]
    ch12 = data[8];
    ch13 = data[12];
    ch14 = data[16];
    ch15 = data[20]
    s = '"' + date + '"' + ';"' + time + '";' + str(ch12) + ';' + str(ch13) + ';' + str(ch14) + ';' + str(ch15) + ';'
    ofile.writelines(s + '\n')
    start += delta;
    ifile.seek(start)
    data = ifile.read(count)
ifile.close()
ofile.close()

# date = str(dt).split()[0]
# time = str(dt).split()[1]
