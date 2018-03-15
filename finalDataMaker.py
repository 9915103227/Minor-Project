import csv
price=open("finalPrice.csv","r")
readerPrice=csv.reader(price)
tweet=open("bitcoinTweet.csv","r")
readerTweet=csv.reader(tweet)
i=0
with open("finalData.csv","wb") as nf:
	min=0
	sum=0.0
	num=0.0
	for linePrice in readerPrice:
		print i
		i=i+1
		if(min==120):
			num=sum/120
			sum=0
			min=0
			for lineTweet in readerTweet:
				if(float(lineTweet[1])<(float(linePrice[0])-7200)):
					continue
				if(float(lineTweet[1])>float(linePrice[0])):
					break
				list=[]
				list.append(lineTweet[2])
				list.append(lineTweet[3])
				list.append(lineTweet[4])
				list.append(lineTweet[5])
				list.append(lineTweet[6])
				list.append(lineTweet[7])
				list.append(lineTweet[8])
				list.append(lineTweet[9])
				list.append(float(linePrice[0])-float(lineTweet[1]))
				list.append(num)
				wr = csv.writer(nf, quoting=csv.QUOTE_ALL);
				wr.writerow(list);
		else:
			sum=sum+float(linePrice[1])
			min=min+1


	num=sum/min
	sum=0
	min=0
	for lineTweet in readerTweet:
		if(float(lineTweet[1])<(float(linePrice[0])-7200)):
			continue
		if(float(lineTweet[1])>float(linePrice[0])):
			break
		list=[]
		list.append(lineTweet[2])
		list.append(lineTweet[3])
		list.append(lineTweet[4])
		list.append(lineTweet[5])
		list.append(lineTweet[6])
		list.append(lineTweet[7])
		list.append(lineTweet[8])
		list.append(lineTweet[9])
		list.append(float(linePrice[0])-float(lineTweet[1]))
		list.append(num)
		wr = csv.writer(nf, quoting=csv.QUOTE_ALL);
		wr.writerow(list);

		
