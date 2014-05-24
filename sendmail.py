#!/usr/bin/python  
#coding:utf8

import os, re, smtplib
from email.utils import COMMASPACE
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from mailInfo import sender, password, subject, tolist, cclist, filespath 

def sendMail(content, filespath = None) :
	try :
		# get server name from email sender
		r_server = re.compile(r'.*@(.*)(\.com|\.cn)')
		server_name = re.findall(r_server, sender)
		smtpserver = 'smtp.' + server_name[0][0] + '.com'
		smtpport = '25'
		username = sender
		# support attachment
		msg = MIMEMultipart()
		if filespath is not None :
			for singlefile in filespath :
				att = MIMEText(open(singlefile, 'rb').read(), 'base64')
				att['content-type'] = 'application/octet-stream'
				att['content-disposition'] = 'attachment;filename="%s"' % os.path.basename(singlefile)
				msg.attach(att)
		# mail body
		body = MIMEText(content)
		msg.attach(body)
		msg['from'] = sender
		msg['to'] = COMMASPACE.join(tolist)
		msg['cc'] = COMMASPACE.join(cclist)
		msg['subject'] = subject
		smtp = smtplib.SMTP()
		smtp.connect(smtpserver, smtpport)
		smtp.login(username, password)
		smtp.sendmail(sender, tolist, msg.as_string())		
		smtp.close()
		return True
	except Exception, errmsg :
		print errmsg
		return False

if __name__ == "__main__" :
	assert type(sender) == str
	assert type(tolist) == list
	assert type(cclist) == list
	assert type(subject) == str
	assert type(content) == str
	assert type(filespath) == list or filespath is None
	if sendMail(content, filespath) :
		print "send mail successfully."
	else :
		print "send mail failed."
