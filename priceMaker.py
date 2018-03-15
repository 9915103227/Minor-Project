import unicodecsv as csv
import time
import datetime
file=open("price.csv","r")
reader=csv.reader(file)
with open("finalPrice.csv","wb") as nf:
	for line in reader:
		list=[]
		t=line[0]
		z=time.mktime(datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S").timetuple()) 
		#list.append(t)
		list.append(z)
		list.append(line[1])
		wr = csv.writer(nf, quoting=csv.QUOTE_ALL);
		wr.writerow(list);