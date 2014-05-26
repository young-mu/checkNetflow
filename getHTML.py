#!/usr/bin/python
#encoding=utf-8

import urllib, urllib2, cookielib
from logInfo import hostURL, postURL, username, password

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
		headers = {'User-Agent':'Mozilla/5.0'}
		# fill in form to be posted (page source, input)
		postData = {'fr':'00', 'id_ip':username, 'pass':password, 'set':'进入'}
		# encode postData
		postData = urllib.urlencode(postData)
		# request post URL with post data, headers and cookie
		request = urllib2.Request(posturl, postData, headers)
		page = urllib2.urlopen(request)
		html = page.read()
		# support Chinese
		html = unicode(html, 'gb2312').encode('utf-8')
		# enter tmp-page
		tmpurl = hosturl + '/monthly.php'
		tmppage = opener.open(tmpurl)
		tmphtml = tmppage.read()
		tmphtml = unicode(tmphtml, 'gb2312').encode('utf-8')
		# enter sub-page
		subpostData = {'start_year':'2014', 'start_month':'05', 'start_day':'01', 'end_year':'2014', 'end_month':'05', 'end_day':'26', 'ip':'219.217.250.185', 'fr':'11', 'set':'查询'}
#		data = {'ip':'219.217.250.185', 'set':'查询'}
		subpostData = urllib.urlencode(subpostData)
		suburl = hosturl + '/monthly_ret.php'
		subrequest = urllib2.Request(suburl, subpostData, headers)
		subpage = urllib2.urlopen(subrequest)
		subhtml = subpage.read()
		subhtml = unicode(subhtml, 'gb2312').encode('utf-8')
		return subhtml
	except Exception, e :
		print str(e)

if __name__ == '__main__' :
	print getHTMLhitsun(hostURL, postURL, username, password)

