import sys
sys.path.append("C:\Python\Scripts\Twitter")
import tweepy
import json


consumer_key="MFW1yG0vsiGliGvl24RWa2c0E"
consumer_secret="N1GIcJFgum44HSfdwEjIny7SC6HAbUbaFObYNR8tQVkvfBNSzP"
access_key="1166499046200160257-8w9K7vfkES3N0dwmAODvnukA4gVIhS"
access_secret="OiusX4PCHjEgxezy42N6Bx1RRuNdQz70RpOdt8QmD0UUl"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

def gettweets(api,username):
    
    tweets=tweepy.Cursor(api.search,q='to:'+username,tweet_mode="extended").items(200)
    tweets_list=[]
    

    for tweet in tweets:
         
                tweets_list.append({
                 
                'poi_name' : tweet.user.screen_name,
                'poi_id' : tweet.user.id,
                'verified' : tweet.user.verified,
                'country' : tweet.user.location,
                'replied_to_tweet_id' : tweet.in_reply_to_status_id,
                'replied_to_user_id' : tweet.in_reply_to_user_id,
                'tweet_text' : tweet.full_text,
                'tweet_lang' : tweet.lang,
                'hashtags' : tweet.entities.get('hashtags'),
                'mentions' : tweet.entities.get('user_mentions'),
                'tweet_urls' : tweet.entities.get('urls'),
                'tweet_emoticons' : tweet.entities.get('symbols'),
                'tweet_date' : str(tweet.created_at),
                'rep_text' : "null",
                'id' : tweet.id,
                'text' : tweet.full_text
                
                })
    
    with open('Tweet.json', 'w', encoding="utf-8") as output:
        json.dump(tweets_list, output, ensure_ascii=False)



gettweets(api,"NarendraModi")
