#!/usr/bin/python
#encoding=utf-8

import sys, string, time, calendar
import mailInfo, logInfo
from getInfo import getInfohitsun
from sendMail import sendMail


# internal functions
def getCurrentTime() :
	localTime = time.localtime(time.time())
	Year = string.atoi( time.strftime('%Y', localTime) )
	Month = string.atoi( time.strftime('%m', localTime) )
	Day = string.atoi( time.strftime('%d', localTime) )
	Weekday = calendar.weekday(Year, Month, Day)
	Time = time.strftime('%H:%M:%S', localTime) 	
	ret = [Year, Month, Day, Weekday, Time]
	return ret

def getProcessedInfo() :
	dictInfo = getInfohitsun()
	balance = dictInfo['balance']
	balance = string.atof(balance[0])
	netflow = dictInfo['netflow']
	netflow = string.atof(netflow[0].replace(',','')) / 1000 / 1000
	deposit = dictInfo['deposit']
	deposit = string.atof(deposit[0])
	ret = [balance, netflow, deposit]
	return ret

def getContent() :
	[balance, netflow, deposit] = getProcessedInfo()
	[Year, Month, Day, Weekday, Time] = getCurrentTime()
	content = '''Hi, all,\n
The netflow of IP address %s has reached [%.2f GB] until %d-%d-%d %s in this month.
Our lab's net balance is [%.2f] and the deposit is [%.2f].\n
----------
This is sended by checkNetflow daemon automaticlally, please don't reply.\n
Thanks,
checkNetflow''' %(logInfo.username, netflow, Year, Month, Day, Time, balance, deposit)
	return content

def printAccount() :
	[balance, netflow, deposit] = getProcessedInfo()
	print "account infomation\n--------------------"
	print "balance \t: %.2f\ndeposit \t: %.2f\nnetflow \t: %.4f GB" %(balance, deposit, netflow)
	print "--------------------"

def printContent() :
	content = getContent()
	print "mail content\n--------------------\n" + content + "\n--------------------"

def printDebug() :
	print "debug information\n--------------------"
	print "host URL \t: %s\npost URL \t: %s" %(logInfo.hostURL, logInfo.postURL)
	print "IP \t\t: %s\nPassword \t: %s" %(logInfo.username, logInfo.password)
	print "Mailsender \t: %s\nMailpasswd \t: %s" %(mailInfo.sender, mailInfo.password)
	print "Tolist \t\t: %s\nCclist \t\t: %s" %(mailInfo.tolist, mailInfo.cclist)
	print "Subject \t: %s\nAttachments \t: %s" %(mailInfo.subject, mailInfo.filespath)
	[Year, Month, Day, Weekday, Time] = getCurrentTime()
	weekdayName = ['Mon', 'Tue', 'Wes', 'Thr', 'Fri', 'Sat', 'Sun']
	print "Date \t\t: %d-%d-%d\nWeekday \t: %s\nTime \t\t: %s" %(Year, Month, Day, weekdayName[Weekday], Time)
	print "--------------------"
	
def sendDirectMail() :
	content = getContent()
	if sendMail(mailInfo.subject, content) :
		print "send mail successfully."
	else :
		print "send mail failed."

def sendRoutineMail() :
	while True :
		time.sleep(1)
		[Year, Month, Day, Weekday, Time] = getCurrentTime()
		# each Monday 00:00:00
		if (Weekday == 0 and Time == '00:00:00') :
			sendDirectMail()

def printUsage() :
	print "usage unavaliable. (usage : ./checkNetflow.py [i|c|d|m|r])"
	print "--------------------"
	print "a - Account information\nc - mail Content\nd - Debug information\nm - send direct Mail\nr - send Routine mail" 
	print "--------------------"


# main control
if (len(sys.argv) == 2 and sys.argv[1] == 'a') :
	printAccount()
elif (len(sys.argv) == 2 and sys.argv[1] == 'c') :
	printContent()
elif (len(sys.argv) == 2 and sys.argv[1] == 'd') :
	printDebug()
elif (len(sys.argv) == 2 and sys.argv[1] == 'm') :
	sendDirectMail()
elif (len(sys.argv) == 2 and sys.argv[1] == 'r') :
	sendRoutineMail()
else :
	printUsage()

	
