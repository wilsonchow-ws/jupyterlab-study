import hashlib
from math import ceil
from dateutil.relativedelta import relativedelta

def datediff(datepart , startdate , enddate):
    if datepart == "year" or datepart == "yy":
        if enddate.month < startdate.month:
            adj = -1
        elif enddate.month == startdate.month and enddate.day > startdate.day:
            adj = -1
        else:
            adj = 0
        return enddate.year - startdate.year + adj
    elif datepart == "quarter" or datepart == "qq":
        return ((enddate.year - startdate.year) * 12 + enddate.month - startdate.month) // 3
    elif datepart == "month" or datepart == "mm":
        return (enddate.year - startdate.year) * 12 + enddate.month - startdate.month
    elif datepart == "day" or datepart == "dd" or datepart == "d":
        return (enddate - startdate).days
    elif datepart == "week" or datepart == "wk":
        return (enddate - startdate).days // 7
    elif datepart == "second" or datepart == "ss":
        return (enddate - startdate).seconds + ((enddate - startdate).days * 24 * 60 * 60)
    elif datepart == "minute" or datepart == "mi":
        return ((enddate - startdate).seconds // 60) + ((enddate - startdate).days * 24 * 60)
    elif datepart == "hour" or datepart == "hh":
        return ((enddate - startdate).seconds // 60 // 60) + ((enddate - startdate).days * 24)

def dateadd(datepart, number, date):
    if datepart == "minute" or datepart == "mi":
        change = datetime.timedelta(minutes=number)
        return date + change
    elif datepart == "hour" or datepart == "hh":
        change = datetime.timedelta(hours=number)
        return date + change
    elif datepart == "second" or datepart == "ss":
        change = datetime.timedelta(seconds=number)
        return date + change
    elif datepart == "millisecond" or datepart == "ms":
        change = datetime.timedelta(milliseconds=number)
        return date + change
    elif datepart == "microsecond" or datepart == "mcs":
        change = datetime.timedelta(microseconds=number)
        return date + change
    elif datepart == "day" or datepart == "dd":
        change = datetime.timedelta(days=number)
        return date + change
    elif datepart == "month" or datepart == "mm":
        return date + relativedelta(months=number)
    elif datepart == "quarter" or datepart == "qq":
        return date + (relativedelta(months=number) * 3)
    elif datepart == "year" or datepart == "yy":
        return date + relativedelta(years=number)

def sha1Hash(toHash):
    try:
        messageDigest = hashlib.sha1()
        stringM = str(toHash)
        byteM = bytes(stringM, encoding='utf')
        messageDigest.update(byteM)
        return messageDigest.hexdigest()
    except TypeError:
        raise "String to hash was not compatible"