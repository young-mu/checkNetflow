#!/usr/bin/python
#encoding=utf-8

import string, time
from getInfo import getInfohitsun
from sendMail import sendMail

# results required from hitsun.hit.edu.cn
dictInfo = getInfohitsun()
balance = dictInfo['balance']
balance = string.atof(balance[0])
netflow = dictInfo['netflow']
netflow = string.atof(netflow[0].replace(',','')) / 1000 / 1000
deposit = dictInfo['deposit']
deposit = string.atof(deposit[0])

# get cuurent date and time
localTime = time.localtime(time.time())
currentTime = time.strftime('%Y-%m-%d %H:%M:%S', localTime)

content = '''Hi, all,\n
The netflow has reached %.2f GB until %s in this month.
Our lab's net balance is %.2f and the deposit is %.2f.\n
Thanks,
checkNetflow daemon''' %(balance, deposit, netflow, currentTime)

if sendMail(content) :
	print "send mail successfully."
else :
	print "send mail failed."

