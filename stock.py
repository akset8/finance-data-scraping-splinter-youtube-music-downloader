import bs4
import urllib2 
import os
import time


os.system("rm -rf *.txt")

sleep_setting = 0.1   ##value in minutes 

urls =["https://in.finance.yahoo.com/q?s=^N225&ql=1",
"https://in.finance.yahoo.com/q?s=%5EHSI&ql=0",
"https://in.finance.yahoo.com/q?s=%5ESSEC",
"https://in.finance.yahoo.com/q?s=%5EFTSE&ql=0",
"https://in.finance.yahoo.com/q?s=%5EFCHI",
"https://in.finance.yahoo.com/q?s=%5EGDAXI",
"https://in.finance.yahoo.com/q?s=%5EDJI&ql=0",
"https://in.finance.yahoo.com/q?s=%5EIXIC"
]



count = 0



while(True):

	f=open(str(count)+".txt","w")
	count=count+1;
	s=""
	f.write("Dear Sir,\n\n")
	for i in range(len(urls)):


		html_doc=urllib2.urlopen(urls[i])

		soup = bs4.BeautifulSoup(html_doc, 'html.parser')
		w=soup.find(attrs={'id':"yfs_market_time"})

		#d =datetime.datetime.now().time()
		#<span id="yfs_market_time">Sat, Oct  3, 2015, 10:03AM EDT - <b>US Markets are closed</b></span>
		#print w.get_text();
		#print w.get_text().find("up")

		r=soup.find(attrs={'class':"time_rtq"})
		r=r.get_text()
		r=r.split(" ")
		for i in range(len(r)):
			r[i]=r[i].encode("utf8")
		print r

		if(w.get_text().find("close")==-1):

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
	f.write(s)
	f.write("\nRegards,\nTeam Mastertrust")
	
	time.sleep(60*sleep_setting)