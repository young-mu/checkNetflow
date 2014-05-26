#!/usr/bin/python
#encoding=utf-8

import re, string, calendar
from getTime import getCurrentTime
from getHTML import hostURL, postURL, subpostURL
from getHTML import username, password
from getHTML import getHTMLhitsun 

def getInfohitsun() :
	[htmlCtx, subhtmlCtx] = getHTMLhitsun(hostURL, postURL, subpostURL, username, password)
	r_balance = re.compile(r">所剩余额:.*?(\d{1,3}\.\d{2}).*?</td>", re.S)
	balance = re.findall(r_balance, htmlCtx)
	balance = string.atof(balance[0])
	r_deposit = re.compile(r">包月存钱罐余额\(元\):.*?(\d{1,3}\.\d{2}).*?</td>", re.S)
	deposit = re.findall(r_deposit, htmlCtx)
	deposit = string.atof(deposit[0])
	# get netflow dict ( format, day:(free, nofree, indoor) )
	netflow = {} 
	[Year, Month, Day, Weekday, Time] = getCurrentTime()
	for day in range(Day) :
		r_string = r'%04d-%02d-%02d 00:00:00</td>.*?>(\d.*?)</td>.*?>(\d.*?)</td>.*?>(\d.*?)</td>' %(Year, Month, day + 1)		
		r_netflow = re.compile(r_string, re.S)
		_netflow = re.findall(r_netflow, subhtmlCtx)
		if (_netflow != []) :
			free = string.atof(_netflow[0][0].replace(',','')) / 1000 / 1000
			nofree = string.atof(_netflow[0][1].replace(',','')) / 1000 / 1000
			indoor = string.atof(_netflow[0][2].replace(',','')) / 1000 /1000
			netflow[day + 1] = (free, nofree, indoor) 
	return [balance, deposit, netflow]	

if __name__ == '__main__' :
	[balance, deposit, netflow] = getInfohitsun()
	assert type(balance) == float 
	assert type(deposit) == float
	assert type(netflow) == dict 
	print "balance \t: " + str(balance)
	print "deposit \t: " + str(deposit)
	print "netflow \t"
	weekdayName = ['Mon', 'Tue', 'Wes', 'Thu', 'Fri', 'Sat', 'Sun']
	[Year, Month, Day, Weekday, Time] = getCurrentTime()
	print "      Date                 free           nofree          indoor"
	print "------------------------------------------------------------------"
	for day in range(Day) :
		weekday = weekdayName[calendar.weekday(Year, Month, day + 1)]
		if (netflow.has_key(day + 1)) :
			print "%04d-%02d-%02d (%s) \t %.4f GB\t %0.4f GB\t %0.4f GB" %(Year, Month, day + 1,weekday, netflow[day+1][0], netflow[day+1][1], netflow[day+1][2]) 

