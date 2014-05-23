#!/usr/bin/python
#encoding=utf-8

import urllib
import urllib2
import cookielib
from loginfo import username, password

# host URL
hostURL = 'http://hitsun.hit.edu.cn' 			
# post URL (page source, action)
postURL = 'http://hitsun.hit.edu.cn/index1.php'

def getHTMLhitsun(hosturl, posturl, username, password) :
	try :
		# set a cookie proceesor 		
		cj = cookielib.LWPCookieJar()
		cookie_support = urllib2.HTTPCookieProcessor(cj)
		opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
		urllib2.install_opener(opener)
		# get cookie from host URL
		h = urllib2.urlopen(hosturl)
		# camouflage as the Mozilla browser
		headers = {'User-Agent' : 'Mozilla/5.0'}
		# fill in form to be posted (page source, input)
		postData = {'fr':'00', 'id_ip':username, 'pass':password, 'set':'进入'}
		# encode postData
		postData = urllib.urlencode(postData)
		# request post URL with post data, headers and cookie
		request = urllib2.Request(posturl, postData, headers)
		page = urllib2.urlopen(request)
		html = page.read()
		return html
	except Exception, e :
		print str(e)

if __name__ == '__main__' :
	print getHTMLhitsun(hostURL, postURL, username, password)

