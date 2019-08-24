from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)

 
