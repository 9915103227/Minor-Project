import json
import demjson
from pprint import pprint
from textblob import TextBlob
import time
import datetime

#import csv
import unicodecsv as csv
#json_data=open("./sample.json").read()

data = json.load(open('1.json','r'))
#data=demjson.encode(open('bitcoin_price.json'))

#pprint(data)

#print data[0]['volume'];
#print data[1]['volume'];
i= len(data);
print(i)
i=i-1
with open('bitcoinTweet.csv', 'wb') as myfile:
	while(i>=0):
		#try:
			x=data[i]['metadata']['iso_language_code']
			if(x!="en"):
				i=i-1
				continue
			list=[];
			#list.append(data[i]['volume'])
			#list.append(data[i]['bid']);
			#list.append(data[i]['created_at'])
			y=data[i]['created_at']
			z=time.mktime(datetime.datetime.strptime(y, "%a %b %d %H:%M:%S +0000 %Y").timetuple()) 
			list.append(z)
			str=TextBlob(data[i]['text']);
			polarity=str.sentiment.polarity
			list.append(polarity)
			#list.append(data[i]['text'])
			#list.append(data[i]['user']['description'])
			x=data[i]['user']['protected']
			if(x=="true"):
				list.append(1)
			else:
				list.append(0)
			x=data[i]['user']['verified']
			if(x=="true"):
				list.append(1)
			else:
				list.append(0)
			
			list.append(data[i]['user']['followers_count'])
			list.append(data[i]['user']['friends_count'])
			list.append(data[i]['user']['favourites_count'])
			list.append(data[i]['user']['statuses_count'])
			list.append(data[i]['retweet_count'])
			
			print(list)
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL);
			wr.writerow(list);
			i=i-1
			print(list)
		#except:
		#	continue
