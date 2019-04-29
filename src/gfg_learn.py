'''
Author: Adil Moujahid
Description: Script for analyzing tweets to compare the popularity of 3 programming languages: Python, Javascript and ruby
Reference: http://adilmoujahid.com/posts/2014/07/twitter-analytics/
'''

import json
import pandas as pd
import matplotlib.pyplot as plt
import re

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy 
import time 
#Variables that contains the user credentials to access Twitter API
access_token = "2737398621-GldBu1iJfHod57VthkSHMa6SJfxn1tPPLoLYu6h"
access_token_secret = "YwHGAf4x13xTPAEvyXvrPD7mfP6GoIUnZyRTtQFxhRcWF"
consumer_key = "rdcH8t1pDEWwxvaYT8ir3gyhS"
consumer_secret = "DrKvpsxJrCFT7suxGyMc9FVOCwiQIcsI7WELw2O4GEKao1IIR2"


 
#This is a basic listener that just prints received tweets to stdout.


class StdOutListener(StreamListener):
    def __init__(self):
        self.count = 0
        self.tweets_data_row =[]
    def on_data(self, data):
        self.tweets_data_row.append(data)
        #self.count = self.count + 1
        #print(self.count)
        return True

    def on_error(self, status):
        print (status)


def main(tweets_data_row):


    #Reading Tweets
    print ('Reading Tweets\n')
    #tweets_data_path = r'G:\4th year CSE\2nd Term\Database\DBproject\data\data.txt'

    tweets_data = []
    #tweets_file = open(tweets_data_path, "r")
    for tweet in tweets_data_row :
        if tweet.strip():  # if it is not a blank line
            try:
                t = json.loads(tweet)
                tweets_data.append(t)
            except:
                continue
    print("reading %d Tweets \n" %len(tweets_data))
    #Structuring Tweets
    print ('Structuring Tweets\n')
    tweets = pd.DataFrame()
##    
    tweets['text'] = [tweet.get('text','None') for tweet in tweets_data]
    tweets['lang'] =[ tweet.get('lang','None') for tweet in tweets_data]
    tweets['date'] =[ tweet.get('created_at','None')for tweet in tweets_data]
    tweets['link'] = ['https://twitter.com/statuses/'+tweet.get('id_str','')
                               for tweet in tweets_data] 
    #we will add a another coulmn which is a tag using ML algorithm 


####################################################################

    ##        try: 
    ##            tweets['country'] = tweet['place']['country']
    ##        except KeyError: 
    ##            tweets['country'] = None

            #tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))
##            if 'user' in tweet.keys():
          #  tweets['user_name'] = [tweet['user']['name'] for tweet in tweets_data]
##            else :
##                tweets['user_name'] = None
         
  
#    tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))

##########################################################################3
#    print(tweets['link'])
#    print(tweets['date'])
    return tweets 




##############################################################################   
##    tweets = [] 
##            # call twitter api to fetch tweets
##    #fetched_tweets = self.api.search(q = query, count = count) 
##  
##            # parsing tweets one by one
##    for tweet in tweets_data: 
##                # empty dictionary to store required params of a tweet 
##                parsed_tweet = {} 
##  
##                # saving text of tweet 
##                parsed_tweet['text'] = tweet.get('text','') 
##                # saving sentiment of tweet 
##                #parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
##  
##                # appending parsed tweet to tweets list
##                if tweet.get('text','') == '' :
##                    continue
##                else:
##                    if tweet['retweet_count'] > 0: 
##                    # if tweet has retweets, ensure that it is appended only once 
##                        if parsed_tweet not in tweets: 
##                            tweets.append(parsed_tweet) 
##                    else: 
##                        tweets.append(parsed_tweet)
##    for tweet in tweets :
##        print(tweet['text'])
##  
if __name__=='__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['2737398621'])
    stream.filter(track=['i', 'the', 'a', 'he', 'she',
                         'him', 'we', 'they', 'this', 'that', 'non' , 'no', 'yes',
                         'for', 'on', 'in', 'to', 'happy' , 'sad' ],is_async = True,
                      follow =['2737398621'] )
    run_time = 7 ;
    time.sleep(run_time)
    stream.disconnect()
    tweets = main(l.tweets_data_row)



