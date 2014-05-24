#!/usr/bin/python
#encoding=utf-8

from getInfo import getInfohitsun

balanceThreshold = 50

dictInfo = getInfohitsun()
balance = dictInfo['balance']
netflow = dictInfo['netflow']
deposit = dictInfo['deposit']

content = '''Hi, all,\n
Our lab's net balance is RMB %s, which is less than threshold RMB %s.
The netflow has reached %s GB until now this month.
The deposit is RMB %s left.\n
Thanks,
checkNetflow daemon''' %(balance, balanceThreshold, netflow, deposit)

print content


