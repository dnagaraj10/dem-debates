
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re
from textblob import TextBlob


# In[2]:


df = pd.read_csv('demDebateCSV')
df = df.head()


# In[3]:


df.dropna(inplace=False)


# In[4]:


text_lines = df['tweet_text'].tolist()


# In[5]:


stoplist = stopwords.words('english')


# In[6]:


only_words = re.sub("[^a-z]", " ", text_lines)
no_single_char = re.sub(r'(?:^| )\w(?:$| )', ' ', only_words).strip()
words1 = no_single_char.split()
words1 = [x.lower() for x in words1]
tweet_corpus = [word for word in words1 if word not in stoplist]


# In[7]:


positive_tweets = [tweet for tweet in tweet_corpus if tweet.sentiment.polarity > 0]
neutral_tweets = [tweet for tweet in tweet_corpus if tweet.sentiment.polarity == 0]
negative_tweets = [tweet for tweet in tweet_corpus if tweet.sentiment.polarity < 0]


# In[8]:


print("Positive Tweets Percentage: {} %".format(100*len(positive_tweets)/len(tweet_corpus)))
print("Neutral Tweets Percentage: {} %".format(100*len(neutral_tweets)/len(tweet_corpus)))
print("Negative Tweets Percentage: {} %".format(100*len(negative_tweets)/len(tweet_corpus)))

