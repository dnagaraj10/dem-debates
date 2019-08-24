import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import csv
import authCodes #.py file with access keys

auth = OAuthHandler(authCodes.CONSUMER_KEY,authCodes.CONSUMER_SECRET)
auth.set_access_token(authCodes.ACCESS_TOKEN,authCodes.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

demDebateCSV = open('demdeb.csv', 'a')
csvWriter = csv.writer(demDebateCSV)

for tweet in tweepy.Cursor(api.search,q="#DemDebate",count=10000, lang="en", since="2019-07-25", tweet_mode='extended').items():
    csvWriter.writerow([tweet.user.screen_name, tweet.text.encode('utf-8')])
 
