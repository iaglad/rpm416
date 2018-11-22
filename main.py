import ftplib
from datetime import datetime


class RPM:
    def __init__(self, ip, login, password):
        self.ip = ip
        self.login = login
        self.password = password
        self.ftp = ftplib.FTP(self.ip, self.login, self.password)

    def ftp2dat(self, path, ofilename):
        self.ftp.cwd(path)
        print(self.ftp.dir())
        f = open(ofilename, 'wb')
        self.ftp.makepasv()
        self.ftp.retrbinary('RETR' + ' FILE0001.RDF', f.write)
        f.close()

    def __del__(self):
        self.ftp.close()


class CSV:
    def __init__(self):
        self.start = 0x68
        self.delta = 0x58
        self.count = 21
        self.base4 = 0x1000000
        self.base3 = 0x10000
        self.base2 = 0x100

    def dat2csv(self, datname, csvname):
        ifile = open(datname, 'rb')
        ofile = open(csvname, 'w')
        ifile.seek(self.start)
        data = ifile.read(self.count)
        while data:
            x = hex(data[7] * self.base4 + data[6] * self.base3 + data[5] * self.base2 + data[4])
            x = int(x, 16) + 1514764800 - 1199232000  # + 10лет - 2 часа
            dt = datetime.utcfromtimestamp(x)
            ch12 = data[8]
            ch13 = data[12]
            ch14 = data[16]
            ch15 = data[20]
            s = '"' + str(dt.day).zfill(2) + '.' + str(dt.month).zfill(2) + '.' + str(dt.year) + '";"' + \
                str(dt.hour).zfill(2) + ':' + str(dt.minute).zfill(2) + ':' + str(dt.second).zfill(2) + '.' + str(dt.microsecond).zfill(3) + '";' + \
                str(ch12) + ';' + str(ch13) + ';' + str(ch14) + ';' + str(ch15) + ';'
            ofile.writelines(s + '\n')
            self.start += self.delta
            ifile.seek(self.start)
            data = ifile.read(self.count)
        ifile.close()
        ofile.close()

class ParsedDT:
    def __init__(self, dt):
        self._dt = dt
        self._year = dt.year
        self._month = dt.month
        self._day = dt.day
        self._hour = dt.hour
        self._minute = dt.minute
        self._second = dt.second
        self._microsecond = dt.microsecond

    @property
    def year(self):
        return self._year.__str__()

    @property
    def year(self):
        return self._year.__str__()

    @property
    def month(self):
        return self._month.__str__()

    @property
    def monthU(self):
        return dt.strftime("%b").upper()

    @property
    def day(self):
        return str(self._day).zfill(2)

    @property
    def hour(self):
        return str(self._hour).zfill(2)

    @property
    def minute(self):
        return str(self._minute).zfill(2)

    @property
    def second(self):
        return str(self._second).zfill(2)

    @property
    def microsecond(self):
        return str(self._microsecond).zfill(3)


if __name__ == "__main__":
    # rpm = RPM('172.16.6.15', 'ftp', 'admin')
    # rpm.ftp2dat('/RPM416/2018/NOV/21', 'd:\\rpm21.dat')
    # rpm.ftp2dat('/RPM416/2018/NOV/19', 'd:\\rpm19.dat')
    #  csv = CSV()
    #  csv.dat2csv('d:\\rpm21.dat', 'd:\\rpm21.csv')
    # csv.dat2csv('d:\\rpm19.dat', 'd:\\rpm19.csv')

    dt = datetime.now()
    dtold = datetime.strptime('08.11.2018', '%d.%m.%Y')

    pdt = ParsedDT(dt)

    # s = '/RPM416/' + dt.year.__str__() + '/' + dt.strftime("%b").upper() + '/' + str(dt.day).zfill(2)
    # s = dt.strftime("%b").upper()

    print(pdt.year, pdt.month, pdt.monthU, pdt.day, pdt.hour, pdt.minute, pdt.second, pdt.microsecond)

