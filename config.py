from pymongo import MongoClient

import tweepy

# config = {}
# execfile("config.py", config)


consumer_key = "XXXXXXXXXXXXXxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token = "xxxxxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxx"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# india woeid , you can use any other country woeid
india_woeid=23424848

mongo_db_name="twitter"
mongo_trending_collection_name="trends"

mongoClient = MongoClient()

mongo_twitter_db=mongoClient[mongo_db_name]



