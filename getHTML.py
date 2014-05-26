#!/usr/bin/python
#encoding=utf-8

import urllib, urllib2, cookielib
from getTime import getCurrentTime
from logInfo import hostURL, postURL, subpostURL, username, password


def getHTMLhitsun(hosturl, posturl, subposturl, username, password) :
	try :
		# 1. set a cookie proceesor 		
		cj = cookielib.LWPCookieJar()
		cookie_support = urllib2.HTTPCookieProcessor(cj)
		opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
		urllib2.install_opener(opener)
		# 2. get cookie from host URL
		h = urllib2.urlopen(hosturl)
		# 3. camouflage as the Mozilla browser
		headers = {'User-Agent':'Mozilla/5.0'}
		# 4. fill in form to be posted (page source, <input> label)
		postData = {'fr':'00', 'id_ip':username, 'pass':password, 'set':'进入'}
		# 5. encode postData
		postData = urllib.urlencode(postData)
		# 6. request post URL with post data, headers and cookie
		request = urllib2.Request(posturl, postData, headers)
		page = urllib2.urlopen(request)
		html = page.read()
		# 7. support Chinese
		html = unicode(html, 'gb2312').encode('utf-8')
		# enter sub-page (post) (normal : page = opener.open(URL)
		[Year, Month, Day, Weekday, Time] = getCurrentTime()
		subpostData = {'start_year':Year, 'start_month':Month, 'start_day':1, 
					   'end_year':Year, 'end_month':Month, 'end_day':Day, 
					   'ip':username, 'fr':'11', 'set':'查询'}
		subpostData = urllib.urlencode(subpostData)
		subrequest = urllib2.Request(subposturl, subpostData, headers)
		subpage = urllib2.urlopen(subrequest)
		subhtml = subpage.read()
		subhtml = unicode(subhtml, 'gb2312').encode('utf-8')
		return [html, subhtml]
	except Exception, e :
		print str(e)

if __name__ == '__main__' :
	assert type(hostURL) == str
	assert type(postURL) == str
	assert type(subpostURL) == str
	assert type(username) == str
	assert type(password) == str
	[html, subhtml] = getHTMLhitsun(hostURL, postURL, subpostURL, username, password)
	assert type(html) == str
	assert type(subhtml) == str
	print "HTML data of %s : \n--------------------" % hostURL
	print html
	print "HTML data of %s : \n--------------------" % subpostURL
	print subhtml
