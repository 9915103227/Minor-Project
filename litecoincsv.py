from bs4 import BeautifulSoup
import csv
import urllib2
import datetime
#url="https://www.seedrs.com/tanorganic"
url="https://www.worldcoinindex.com/coin/litecoin"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = urllib2.Request(url, headers=hdr)
with open('liteprice.csv', 'wb') as myfile:
	while(1):
		page = urllib2.urlopen(req)
		soup = BeautifulSoup(page.read(), "html.parser")
		target = soup.find("td", class_="coinprice")
		text=target.text.strip()
		#print text.strip('\n');
		l=len(text)
		n=""
		for i in range(l):
			c=text[i]
			if(c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9' or c=='0' or c=='.'):
				n=n+c
		#print n
		list=[]
		list.append(n)
		#dt=datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S %Z %Y")
		dt=datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S");
		#print dt
		list.append(dt)
		
		#2018-02-20-13-13-12
		#Sat Oct 04 13:00:36  2014
		#print target.text.strip()
		text=soup.find("td",class_="coin-high").text.strip()
		l=len(text)
		n=""
		for i in range(l):
			c=text[i]
			if(c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9' or c=='0' or c=='.'):
				n=n+c
		list.append(n);

		text=soup.find("td",class_="coin-low").text.strip()
		l=len(text)
		n=""
		for i in range(l):
			c=text[i]
			if(c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9' or c=='0' or c=='.'):
				n=n+c
		list.append(n);

		text=soup.find("td",class_="coin-volume").text.strip()
		l=len(text)
		n=""
		for i in range(l):
			c=text[i]
			if(c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9' or c=='0' or c=='.'):
				n=n+c
		list.append(n);

		text=soup.find("td",class_="coin-supply").text.strip()
		l=len(text)
		n=""
		for i in range(l):
			c=text[i]
			if(c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9' or c=='0' or c=='.'):
				n=n+c
		list.append(n);

		text=soup.find("td",class_="coin-marketcap").text.strip()
		l=len(text)
		n=""
		for i in range(l):
			c=text[i]
			if(c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9' or c=='0' or c=='.'):
				n=n+c
		list.append(n);
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL);
		wr.writerow(list);

'''FORMAT
	price;	24-high;	24-low;	24-Volume;	#Coins(Millions);	Market_Cap(Billions)
'''