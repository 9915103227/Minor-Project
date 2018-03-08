import json
import demjson
from pprint import pprint
from textblob import TextBlob
#import csv
import unicodecsv as csv
#json_data=open("./sample.json").read()

data = json.load(open('bitcoinTweet.json','r'))
#data=demjson.encode(open('bitcoin_price.json'))

#pprint(data)

#print data[0]['volume'];
#print data[1]['volume'];
l= len(data);
print(l)
with open('bitcoinTweet.csv', 'wb') as myfile:
	for i in range(l):
		try:
			list=[];
			#list.append(data[i]['volume'])
			#list.append(data[i]['bid']);
			list.append(data[i]['created_at'])
			str=TextBlob(data[i]['text']);
			polarity=str.sentiment.polarity
			list.append(polarity)
			#list.append(data[i]['text'])
			list.append(data[i]['user']['description'])
			list.append(data[i]['user']['protected'])
			list.append(data[i]['user']['verified'])
			list.append(data[i]['user']['followers_count'])
			list.append(data[i]['user']['friends_count'])
			list.append(data[i]['user']['favourites_count'])
			list.append(data[i]['user']['statuses_count'])
			print(list)
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL);
			wr.writerow(list);
		except:
			continue
		
