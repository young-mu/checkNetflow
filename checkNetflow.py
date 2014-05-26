#!/usr/bin/python
#encoding=utf-8

import sys, string
import mailInfo, logInfo
from getTime import getCurrentTime
from getInfo import getInfohitsun
from sendMail import sendMail

# internal functions
def getNetflow(netflow) :
	values = netflow.values();
	free = 0.0
	nofree = 0.0
	indoor = 0.0
	for i in range(len(values)) :
		free += values[i][0]
		nofree += values[i][1]
		indoor += values[i][2]
	total = free + nofree + indoor
	return [total, free, nofree, indoor]
		
def getContent() :
	[balance, deposit, netflow] = getInfohitsun()
	[total, free, nofree, indoor] = getNetflow(netflow)	
	[Year, Month, Day, Weekday, Time] = getCurrentTime()
	content = '''Hi, all,\n
Until %d-%d-%d %s in this month, the total netflow has reached [%.2f GB].
The free, nofree and indoor netflow are [%.2f GB], [%.2f GB] and [%.2f GB] respectively. 
Our lab's net balance is [%.2f] and the deposit is [%.2f].\n
---------------
This is sended by checkNetflow daemon automaticlally, please don't reply.\n
Thanks,
checkNetflow''' %(Year, Month, Day, Time, total, free, nofree, indoor, balance, deposit)
	return content

def printAccount() :
	[balance, deposit, netflow] = getInfohitsun()
	[total, free, nofree, indoor] = getNetflow(netflow)
	print "account infomation\n--------------------"
	print "balance \t\t: %.2f\ndeposit \t\t: %.2f\nnetflow (total)\t\t: %.4f GB" %(balance, deposit, total)
	print "netflow (free) \t\t: %.4f GB\nnetflow (nofree) \t: %.4f GB\nnetflow (indoor) \t: %.4f GB" %(free, nofree, indoor)
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
	print "Date \t\t: %d-%d-%d\nWeekday \t: %s\nTime \t\t: %s" %(Year, Month, Day, Weekday, Time)
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
if __name__ == '__main__' :
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

	
