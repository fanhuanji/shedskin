from time import struct_time

MINYEAR = 1
MAXYEAR = 9999

class date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def today():
        return date(0, 0, 0)
    
    def fromtimestamp(timestamp):
        return date(0, 0, 0)
    
    def fromordinal(ordinal):
        return date(0, 0, 0)
    
    today         = staticmethod(today)
    fromtimestamp = staticmethod(fromtimestamp)
    fromordinal   = staticmethod(fromordinal)
    
    def __add__(self, other):
        return self

    def __sub__(self, other):
        return other.subfromdate()

    def subfromdate(self):
        return timedelta()
    
    def replace(self, year=0, month=0, day=0):
        return self
    
    def timetuple(self):
        return struct_time(9*(1,))

    def toordinal(self):
        return 1
    
    def weekday(self):
        return 1

    def isoweekday(self):
        return 1

    def isocalendar(self):
        return (1, 1, 1)

    def isoformat(self):
        return ''
    
    def __str__(self):
        return ''

    def ctime(self):
        return ''

    def strftime(self, format):
        return ''

class datetime(date):
    def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=0):
        date.__init__(self, year, month, day)

        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.tzinfo = tzinfo
    
    def today():
        return datetime(0, 0, 0)
    
    def now(tz=0):
        return datetime(0, 0, 0)
    
    def utcnow():
        return datetime(0, 0, 0)
    
    def fromtimestamp(timestamp, tz):
        return datetime(0, 0, 0)
    
    def utcfromtimestamp(timestamp):
        return datetime(0, 0, 0)
    
    def fromordinal(ordinal):
        return datetime(0, 0, 0)
    
    def combine(date, time):
        return datetime(0, 0, 0)
    
    def strptime(date_string, format):
        return datetime(0, 0, 0)

    today = staticmethod(today)
    now = staticmethod(now)
    utcnow = staticmethod(utcnow)
    fromtimestamp = staticmethod(fromtimestamp)
    utcfromtimestamp = staticmethod(utcfromtimestamp)
    fromordinal = staticmethod(fromordinal)
    combine = staticmethod(combine)
    strptime = staticmethod(strptime)
    
    def __add__(self, delta):
        return self

    def __sub__(self, other):
        return other.subfromdatetime()
    
    def subfromdatetime(self):
        return timedelta()
    
    def date(self):
        return date(self.year, self.month, self.day)

    def time(self):
        return time(self.hour, self.minute, self.second, self.microsecond, 0)

    def timetz(self):
        return time(self.hour, self.minute, self.second, self.microsecond, self.tzinfo)

    def replace(self, year=0, month=0, day=0, hour=0, minute=0, second=0, microsecond=0, tzinfo=0):
        return self

    def astimezone(self, tz):
        return self

    def utcoffset(self):
        return timedelta()

    def dst(self):
        return timedelta()

    def tzname(self):
        return ''

    def timetuple(self):
        return struct_time(9*(1,))

    def utctimetuple(self):
        return struct_time(9*(1,))

    def toordinal(self):
        return 1

    def weekday(self):
        return 1

    def isoweekday(self):
        return 1

    def isocalendar(self):
        return (1, 1, 1)

    def isoformat(self, sep):
        return ''

    def __str__(self):
        return ''

    def ctime(self):
        return ''

    def strftime(self, format):
        return ''

class time:
    def __init__(self, hour, minute, second, microsecond, tzinfo=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.tzinfo = tzinfo
    
    def replace(self, hour=0, minute=0, seconds=0, microseconds=0, tzinfo=0):
        return self

    def isoformat(self):
        return ''

    def __str__(self):
        return ''

    def strftime(self, format):
        return ''

    def utcoffset(self):
        return timedelta()

    def dst(self):
        return timedelta()

    def tzname(self):
        return ''

class timedelta:
    def __init__(self, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        self.days = 1
        self.seconds = 1
        self.microseconds = 1
    
    def __str__(self):
        return ''

    def __add__(self, other):
        return self

    def __sub__(self, other):
        return self

    def __mul__(self, n):
        return self

    def __div__(self, n):
        return self
    
    def __neg__(self):
        return self

    def __floordiv__(self, n):
        return self

    def __abs__(self):
        return self
    
    def subfromdate(self):
        return date(1, 1, 1)

    def subfromdatetime(self):
        return datetime(1, 1, 1)

date.min = date (MINYEAR, 1, 1)
date.max = date (MAXYEAR, 12, 31)
date.resolution = timedelta(days=1)

datetime.min = datetime(MINYEAR, 1, 1, tzinfo=0)
datetime.max = datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999, tzinfo=0)
datetime.resolution = timedelta(microseconds=1)

time.min = time(0, 0, 0, 0)
time.max = time(23, 59, 59, 999999)
time.resolution = timedelta(microseconds=1)

timedelta.min = timedelta(-999999999)
timedelta.max = timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)
timedelta.resolution = timedelta(microseconds=1)
    

'''if __name__ == "__main__":
    #datetime.date tests
    
    d2 = date.today()
    d3 = date.fromtimestamp(1234)
    d4 = date.fromordinal(123)

    d1 = date(2008, 01, 01)
    d2 = date(2005, 05, 06)
    d3 = d1 + timedelta(days=1)
    d4 = d3 - timedelta(days=1)
    d4 == d1
    d4 != d2
    d3 >= d4
    d3 > d4
    d3 <= d1
    d1 < d1
    d5 = d1.replace(year=2222)
    d5.toordinal()
    str(d5)
    d5.isoformat()
    d5 = d1.replace(year=2007)
    d6 = d1 + timedelta(days=1)
    td1 = d1 - d5
    
    d1.isocalendar()
    d1.timetuple()
    d1.weekday()
    d1.isoweekday()
    d1.ctime()
    d1.strftime('')

    #datetime.time tests
    
    t1 = time(12, 01, 01, 01)
    t2 = t1.replace(hour=9)
    t1.isoformat()
    str(t2)
    
    t1 == t2
    t1 != t2
    t1 >= t2
    t1 >  t2
    t1 <= t2
    t1 <  t2

    t1.strftime('')
    t1.utcoffset()
    t1.dst()
    t1.tzname()

    #datetime.datetime tests
    
    dt1 = datetime(2008, 01, 01)
    dt4 = datetime.utcnow()
    dt5 = datetime.strptime("", "")
    dt6 = datetime.utcfromtimestamp(111)
    dt7 = datetime.combine(d1, t1)
    dt8 = datetime.now()

    d99 = datetime.today()
    d98 = datetime.fromtimestamp(1234, 2)
    d97 = datetime.fromordinal(123)

    dt2 = dt1 + timedelta(days=1)
    td1 = dt2 - dt1
    dt2 - td1 # XXX test this
    d10 = dt1.date()
    t10 = dt1.time()
    t11 = dt1.timetz()
    dt2 = dt1.replace(year=100)
    dt2.isoformat(' ')
    str(dt1)
    
    dt1 == dt2
    dt1 != dt2
    dt1 >= dt2
    dt1 >  dt2
    dt1 <= dt2
    dt1 <  dt2

    dt1.weekday()
    dt1.utctimetuple()
    dt1.toordinal()
    dt1.astimezone(1) # XXX needs arg
    dt1.strftime('')
    dt1.dst()
    dt1.isocalendar()
    dt1.timetuple()
    dt1.tzname()
    dt1.isoweekday()
    dt1.utcoffset()
    dt1.ctime()

    #datetime.timedelta tests
    
    td1 = timedelta(days=1)
    td2 = timedelta(hours=2)
    td3 = td1 + td2
    td4 = td1 - td2
    td5 = td1 * 4
    td6 = td2 / 2
    str(td1)

    td1 != td2
    abs(td1)
    td7 = td1 // 2
    td1 == td2
    td8 = -td1'''
