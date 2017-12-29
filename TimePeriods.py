from datetime import datetime, date, time, timedelta
import time as pyTime
import math

CONST_24HRS = 86400;
CONST_WEEK = 604800;
CONST_MONTH = 2592000;

def last24 ():
    now = math.floor(pyTime.time());
    dayAgo = math.floor(pyTime.time())-CONST_24HRS;
    return (now,dayAgo)

def yesterday():
    midnight = pyTime.mktime(datetime.timetuple(datetime.combine(date.today(),time.min)));
    lastMidnight = midnight - CONST_24HRS;
    return(midnight, lastMidnight)

def getDay(offset):
    midnight = pyTime.mktime(datetime.timetuple(datetime.combine(date.today(),time.min)));
    lastMidnight = midnight - CONST_24HRS;
    return(midnight-(CONST_24HRS*offset), lastMidnight-(CONST_24HRS*offset))

def lastWeek():
    now = math.floor(pyTime.time());
    weekAgo = now - CONST_WEEK;
    return(now,weekAgo)

def lastCalendarWeek():
    mondayDate = date.today() - timedelta(days=date.today().weekday());
    mondayUTC = pyTime.mktime(mondayDate.timetuple());
    lastMonday = mondayUTC - CONST_WEEK;
    return(mondayUTC,lastMonday)

def lastMonth():
    now = math.floor(pyTime.time());
    monthAgo = now - CONST_MONTH;
    return(now,monthAgo)
