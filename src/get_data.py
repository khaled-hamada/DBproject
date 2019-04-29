#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy 

#Variables that contains the user credentials to access Twitter API
access_token = "2737398621-GldBu1iJfHod57VthkSHMa6SJfxn1tPPLoLYu6h"
access_token_secret = "YwHGAf4x13xTPAEvyXvrPD7mfP6GoIUnZyRTtQFxhRcWF"
consumer_key = "rdcH8t1pDEWwxvaYT8ir3gyhS"
consumer_secret = "DrKvpsxJrCFT7suxGyMc9FVOCwiQIcsI7WELw2O4GEKao1IIR2"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['2737398621'])
    stream.filter(track=['i', 'the', 'a', 'he', 'she',
                         'him', 'we', 'they', 'this', 'that', 'non' , 'no', 'yes',
                         'for', 'on', 'in', 'to', 'happy' , 'sad' ], follow =['2737398621'])



################################################################
##
##    query = ['i', 'the', 'a', 'he', 'she',
##                         'him', 'we', 'they', 'this' ]
##    count = 2000;
##    #try:
##    # create OAuthHandler object
##    auth = OAuthHandler(consumer_key, consumer_secret)
##            # set access token and secret
##    auth.set_access_token(access_token, access_token_secret)
##            # create tweepy API object to fetch tweets
##    api = tweepy.API(auth)
##    #except:
##    #print("Error: Authentication Failed")
##    # call twitter api to fetch tweets
##    tweets_data = api.search(q = query, count = count)
##
##
##    print("reading %d Tweets \n" %len(tweets_data))
##    #Structuring Tweets
##    print ('Structuring Tweets\n')
##    tweets = pd.DataFrame()
####    for tweet in tweets_data:
####        tweets['text'] = tweet.get('text', '')
####        tweets['lang'] = tweet.get('lang', '')
####        try:
####            tweets['country'] = tweet['place']['country']
####        except KeyError:
####            tweets['country'] = None
##
##    for tweet in tweets_data :
##       # if  tweet.is_quote_status :
##       #     continue 
####            if tweet.text not in tweets['text']:
####                tweets['text'] = tweet.text
####                tweets['lang'] = tweet.lang
####                tweets['date'] = tweet.created_at
####                tweets['link'] = 'https://twitter.com/statuses/'+tweet.id_str
##
##      #  else :
##            tweets['text'] = tweet.text
##            tweets['lang'] = tweet.lang
##            tweets['date'] = tweet.created_at
##            tweets['link'] = 'https://twitter.com/statuses/'+tweet.id_str
##
##
##
##    print(tweets['link'])
