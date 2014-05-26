#!/usr/bin/python
#encoding=utf-8

import string
import time
import calendar 

def getCurrentTime() :
	localTime = time.localtime(time.time())
	Year = string.atoi( time.strftime('%Y', localTime) )
	Month = string.atoi( time.strftime('%m', localTime) )
	Day = string.atoi( time.strftime('%d', localTime) )
	Weekday = calendar.weekday(Year, Month, Day)
	Time = time.strftime('%H:%M:%S', localTime) 	
	ret = [Year, Month, Day, Weekday, Time]
	return ret

if __name__ == '__main__' :
	[Year, Month, Day, Weekday, Time] = getCurrentTime()
	assert type(Year) == int 
	assert type(Month) == int
	assert type(Day) == int
	assert type(Weekday) == int
	assert type(Time) == str
	weekdayName = ['Mon', 'Tue', 'Wes', 'Thr', 'Fri', 'Sat', 'Sun']
	print "Date \t\t: %04d-%02d-%02d\nWeekday \t: %s\nTime \t\t: %s" %(Year, Month, Day, weekdayName[Weekday], Time)
	
