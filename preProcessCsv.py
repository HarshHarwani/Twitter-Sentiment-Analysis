import csv
import sys
import re
def processTweets(tweet):
	tweet=tweet.lower()
	#removing the url's and any web address
	tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
	#removing usernames followed by @
	tweet = re.sub('@[^\s]+','',tweet)
	tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	tweet=re.sub('(?<=\w)\.(?=\w+\.)|\G\w+\K\)','',tweet)
	#removing extra dotes
	tweet=re.sub('[\d\.]',"",tweet)
	#removing special characters like !,<,>,|,@
	tweet=re.sub('[!-><|@]',"",tweet)
	return tweet

#opening the csv file given as an argument and writing the cleaned tweets in a text file	
f = open(sys.argv[1], 'rt')
target=open("cleanedData.txt","w")
try:
    reader = csv.reader(f)
    for row in reader:
	if row[1]=="1":
	   sentiment="positive"
	else:
	   sentiment="negative"
        target.write(row[0]+"|"+sentiment+"|"+" ".join(processTweets(row[3]).split()))
	target.write("\n")
finally:
    f.close()
    target.close()


