#!/usr/bin/python
#encoding=utf-8

import sys, string, time
import mailInfo, logInfo
from getInfo import getInfohitsun
from sendMail import sendMail

# get cuurent date and time
localTime = time.localtime(time.time())
currentTime = time.strftime('%Y-%m-%d %H:%M:%S', localTime)

# results required from hitsun.hit.edu.cn
dictInfo = getInfohitsun()
balance = dictInfo['balance']
balance = string.atof(balance[0])
netflow = dictInfo['netflow']
netflow = string.atof(netflow[0].replace(',','')) / 1000 / 1000
deposit = dictInfo['deposit']
deposit = string.atof(deposit[0])

# mail content
content = '''Hi, all,\n
The netflow has reached %.2f GB until %s in this month.
Our lab's net balance is %.2f and the deposit is %.2f.\n
Thanks,
checkNetflow daemon''' %(netflow, currentTime, balance, deposit)


if (len(sys.argv) == 2 and sys.argv[1] == 'a') :
	print "account infomation\n--------------------"
	print "balance \t: %.2f\ndeposit \t: %.2f\nnetflow \t: %.4f GB" %(balance, deposit, netflow)
	print "--------------------"
elif (len(sys.argv) == 2 and sys.argv[1] == 'c') :
	print "mail content\n--------------------\n" + content + "\n----------"
elif (len(sys.argv) == 2 and sys.argv[1] == 'd') :
	print "debug information\n--------------------"
	print "host URL \t: %s\npost URL \t: %s" %(logInfo.hostURL, logInfo.postURL)
	print "IP \t\t: %s\nPassword \t: %s" %(logInfo.username, logInfo.password)
	print "Mailsender \t: %s\nMailpasswd \t: %s" %(mailInfo.sender, mailInfo.password)
	print "Tolist \t\t: %s\nCclist \t\t: %s" %(mailInfo.tolist, mailInfo.cclist)
	print "Subject \t: %s\nAttachments \t: %s" %(mailInfo.subject, mailInfo.filespath)
	print "--------------------"
elif (len(sys.argv) == 2 and sys.argv[1] == 'm') :
	if sendMail(mailInfo.subject, content) :
		print "send mail successfully."
	else :
		print "send mail failed."
else :
	print "usage unavaliable. (usage : ./checkNetflow.py [i|c|d|m])"
	print "a - Account information | c - mail Content | d - Debug information | m - send Mail" 

