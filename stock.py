import bs4
import urllib2 
import os
import time
import smtplib
import yagmail

##mail wala code already hai mere paas 

from email.mime.text import MIMEText

def send_email(user, pwd, recipient, subject, body):
    

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.ehlo() 
    server_ssl.login(gmail_user, gmail_pwd)  
    server_ssl.sendmail(FROM, TO, message)

    server_ssl.close()
    
    print "hello"
   




os.system("rm -rf *.txt")

sleep_setting = 60  ##value in minutes 

urls =[["https://in.finance.yahoo.com/q?s=^N225&ql=1","https://www.google.com/finance?q=INDEXNIKKEI%3ANI225&ei=Sv0RVtnuF4u1ugT-sY1I"],

["https://in.finance.yahoo.com/q?s=%5EHSI&ql=0","https://www.google.com/finance?q=INDEXHANGSENG%3AHSI&ei=8BgSVuCJHMamuATMgp9Y"],
["https://in.finance.yahoo.com/q?s=%5ESSEC","https://www.google.com/finance?q=SHA%3A000001&ei=6hkSVsnQB4jxugSXyZCIBQ"],
["https://in.finance.yahoo.com/q?s=%5EFTSE&ql=0","https://www.google.com/finance?q=INDEXFTSE%3AUKX&ei=DhoSVuGPGsv2ugSkor1Q"],
["https://in.finance.yahoo.com/q?s=%5EFCHI","https://www.google.com/finance?q=INDEXEURO%3APX1&ei=DhoSVuGPGsv2ugSkor1Q"],
["https://in.finance.yahoo.com/q?s=%5EGDAXI","https://www.google.com/finance?q=INDEXDB%3ADAX&ei=lhoSVpGsNdOhuATtr6CADA"],
["https://in.finance.yahoo.com/q?s=%5EDJI&ql=0","https://www.google.com/finance?q=INDEXDJX%3A.DJI&ei=lhoSVpGsNdOhuATtr6CADA"],
["https://in.finance.yahoo.com/q?s=%5EIXIC","https://www.google.com/finance?q=INDEXNASDAQ%3A.IXIC&ei=0hoSVtmqBM6auATm-q-YAQ"]

]

urls2 = 'http://sgxnifty.org/'

count = 0



while(True):

	
	count=count+1;
	s=""
	s+="Dear Sir,\n\n"
	


	html_doc2=urllib2.urlopen(urls2)
	#html_doc1=urllib2.urlopen(urls[i][1])

	soup2 = bs4.BeautifulSoup(html_doc2, 'html.parser')  #yahoo wala

	#soup1 =bs4.BeautifulSoup(html_doc1, 'html.parser') #google wala 

	print "SGX NIFTY  ",
	s+="SGX NIFTY  "
	x1= soup2.find("td",class_="indexprice")
	x2= soup2.find("td",class_="indexchange")
	print x1.get_text(),
	s+=x1.get_text()
	if(x2.get_text()[0]=="+"):
		print "   UP BY",
		s+="   UP BY"
	else:
		print "   DOWN BY",
		s+="   DOWN BY"

	print "   ",x2.get_text()[1:]," pts"
	s+="   "+x2.get_text()[1:]+"  pts\n\n"


	for i in range(len(urls)):


		html_doc=urllib2.urlopen(urls[i][0])
		html_doc1=urllib2.urlopen(urls[i][1])

		soup = bs4.BeautifulSoup(html_doc, 'html.parser')  #yahoo wala

		soup1 =bs4.BeautifulSoup(html_doc1, 'html.parser') #google wala 

		

		w=soup1.find(attrs={'id':"price-panel"})
		
		

		#d =datetime.datetime.now().time()
		#<span id="yfs_market_time">Sat, Oct  3, 2015, 10:03AM EDT - <b>US Markets are closed</b></span>
		#print w.get_text();
		#print w.get_text().find("up")

		

		if(w.get_text().encode('utf8').find("Close")==-1):

			a=soup.find(attrs={'class':"title"})
			print a.get_text()
			s=s+a.get_text()+"\n"
			

			b=soup.find(attrs={'class':"time_rtq_ticker"})
			print b.get_text(),
			s=s+b.get_text()
		#<span class="time_rtq_ticker" id="yui_3_9_1_8_1443820591320_43"><span id="yfs_l84_aapl">110.38</span></span>


			c=soup.find(attrs={'class':"up_g time_rtq_content"})
			#print c

			if(c!=None):
				print " UP BY " ,
				print c.get_text(),
				s=s+"  up by "
				print len(c.get_text())

				s=s+c.get_text()[:8]
				s=s+" pts"

				

				
				

			d=soup.find(attrs={'class':"down_r time_rtq_content"})
			if(d!=None):
				print " DOWN BY",
				print d.get_text(),
				s=s+"  down by "
				s=s+d.get_text()[:8]
				s=s+" pts"

			e=soup.find(attrs={'class':"time_rtq"})
			print e.get_text()
			
			s=s+e.get_text()+"\n\n"
			print 


			


			
			

	#print s

	s+="\nRegards,\nTeam Mastertrust"
	
	

	print s
	##the email portion here do that





# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
#fp = open(textfile, 'rb')
# Create a text/plain message
	# msg = MIMEText(s)


	# # me == the sender's email address
	# # you == the recipient's email address
	# me = "akshay14133@iiitd.ac.in"
	# you ="creativecreationsvikaspuri@gmail.com"

	# msg['Subject'] = 'market current rates'
	# msg['From'] = me
	# msg['To'] = you

	
	# s = smtplib.SMTP('localhost')
	# s.sendmail(me, [you], msg.as_string())
	# s.quit()

	send_email('ccakshay59@gmail.com', '9313501562','techwave50@gmail.com','stock prices', s )



	time.sleep(60*sleep_setting)


	


#somehow get the emailing to work properly 
#sleep the code so that it wakes up after a given predefined 



