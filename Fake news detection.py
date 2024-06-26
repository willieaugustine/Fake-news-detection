import tweepy
import pandas as pd
import nltk
import re


consumer_key = 'Ncq55A71gRVigy6mXZ7JTq4kC'
consumer_secret = 'Tz0MChm2q7Dt6rTOES9NWIV0xIBTJqLvmcJOVygu5B9hEyP7EP'
access_token = '725028370522710017-2LQG8idx0i1kDmTpq8YZIO5vxIm9PH0'
access_token_secret = 'dM0gP1sXOiUHbbJFaonvkvenFnR83x7aZkNPH8FDV4pi'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def fetch_tweets(query, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(count)
    tweet_list = [[tweet.text] for tweet in tweets]
    return pd.DataFrame(tweet_list, columns=['tweet'])
data = fetch_tweets('COVID-19 vaccine', count=200)
print(data.head())

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words('english')]
    return ''.join(words)
data['cleaned_tweet'] = data['tweet'].apply(preprocess_text)
print(data.head)