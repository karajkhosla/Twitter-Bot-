import requests  
import json  
import tweepy  
import time
import os
import sys
import random
from termcolor import colored



consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)  

volunteertwitterhandle = "funky_entrepreneur"
searchterms = ["#Entrepreneur", "#Entrepreneur2020", "@funky_entrepreneur", "Entrepreneurindia"]

TWEETS = [] 
NAMES = []   

# Follows all the followers
for follower in tweepy.Cursor(API.followers).items(100):
    follower.follow()


while True:
    for searchterm in searchterms:
        for tweet in tweepy.Cursor(API.search, q=searchterm).items(10):
            if tweet in TWEETS:
                pass
            else:
                TWEETS.append(tweet.text)
                if tweet.author.id not in NAMES:
                    NAMES.append(tweet.author.id)
                try:
                    # retweet the tweet with searchterms
                    tweet.retweet()
                    # likes the tweet with searchterms
                    tweet.favorite()
                    # Prevents from retweeting its own tweets
                    if smart_str(tweet.author.screen_name) != volunteertwitterhandle:
                        #retweeting with comment
                        twitter = "https://twitter.com"
                        url = twitter + "/" + tweet.author.screen_name+\
                              "/" + "status" + "/" + str(tweet.id)
                        perfect = smart_str("#Entrepreneur2020"+ " " +\
                                            "#Entrepreneurindia" + " " +\
                                            "\n" +  url)
                        API.update_status(perfect)
                        print("Retweeted with comment of -" +tweet.author.screen_name)
                except tweepy.TweepError:
                    pass

    for i in NAMES:
        try:
        # Following the person who tweeted with #Entrepreneur
            API.create_friendship(i)
        except tweepy.TweepError:
            pass
    time.sleep(15)		
	
	