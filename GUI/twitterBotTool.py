import json 
import csv 
import tweepy 
import re
import timeit 
import numpy as np 
import tweepyListener as tl 

class HeavensDoor: 

    def __init__(self, consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None):

        self.consumer_key = "pQ9HyAWJfLFcNLnAfKwRE168p"
        self.consumer_secret = "WncblPIWdsLQIl7pNjy9MqLlGYHAparajjH65jPYhivQzbdeDg" 
        self.access_token = "1187900179883679745-g63YFJ07goNk6ntP9S807GZw2RfOUs"
        self.access_token_secret = "cZXX56mcGffFwhr8bV7R7SIrPrQprfauEhzmvwNnn1psd"

        if consumer_key != None: 
            self.consumer_key = consumer_key
        if consumer_secret != None: 
            self.consumer_secret = consumer_secret
        if access_token != None: 
            self.access_token = access_token
        if access_token_secret != None: 
            self.access_token_secret = access_token_secret

        #create authentication for accessing Twitter
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)

        #initialize Tweepy API
        self.api = tweepy.API(self.auth)

        # Initialize self data: 
        self.my_id = self.api.me().id_str
        self.screen_name = self.api.me().screen_name

    
    def tweet(self, message): 

        self.api.update_status(message)
    
    def reply_tweet(self, message, tweet_id, user_screen_name): 

        self.api.update_status("@{} {}".format(user_screen_name, message), [tweet_id]) 

    def retweet(self, tweet_id): 

        self.api.retweet(tweet_id) 

    def follow(self, user_id, screen_name): 

        friendship_status = self.api.show_friendship(self.my_id, self.screen_name, user_id, screen_name)
        my_friendship = friendship_status[0] 
        following = my_friendship.following
        followed_by = my_friendship.followed_by
        
        print("{} following {} is {}\n{} is followed by {} is {}".format(self.screen_name, screen_name, following, self.screen_name, screen_name, followed_by))

        if following == False: 
            self.api.create_friendship(user_id)


    def getUserIDAndScreenName(self, username): 

        user_id = self.api.get_user(username).id_str
        screen_name = self.api.get_user(username).screen_name
        print(self.api.get_user(username))
        return user_id, screen_name


# Testing main block 
if __name__ == "__main__": 

    main() 

def main(): 

   instance = HeavensDoor()

   
   

