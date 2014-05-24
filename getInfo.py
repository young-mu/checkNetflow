#!/usr/bin/python
#encoding=utf-8

import re
from getHTML import hostURL, postURL
from getHTML import username, password
from getHTML import getHTMLhitsun 

def getInfohitsun() :
	htmlctx = getHTMLhitsun(hostURL, postURL, username, password)
	r_balance = re.compile(r">所剩余额:.*?(\d{1,3}\.\d{2}).*?</td>", re.S)
	balance = re.findall(r_balance, htmlctx)
	r_netflow = re.compile(r">包月已使用流量\(KB\):.*?(\d.*?\.\d{2}).*?</td>", re.S);
	netflow = re.findall(r_netflow, htmlctx)
	r_deposit = re.compile(r">包月存钱罐余额\(元\):.*?(\d{1,3}\.\d{2}).*?</td>", re.S)
	deposit = re.findall(r_deposit, htmlctx)
	dictInfo = {}
	dictInfo['balance'] = balance
	dictInfo['netflow'] = netflow
	dictInfo['deposit'] = deposit
	return dictInfo	

if __name__ == '__main__' :
	print getInfohitsun()	
