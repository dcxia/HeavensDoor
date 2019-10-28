import twitterBotTool as tbtool
import tweepyListener as tl
import numpy as np 
from matplotlib import pyplot as plt 
import tkinter as tk 
import time 

# Initialize global save state of tweet data: 
tweets = tl.continuous_tweets

'''
HOW TO USE: 
1. Initialize with twitterBotTool() object as done below in the first line of the main function. 
2. Call main() function of tweepyListener.py to start the listener for keywords in format of a list...ex keywords=['jetblue','jetblue stocks', 'united airlines'] 
3. Global variable of tweepyListener, 
            continuous_tweets = [] 
    is a list variable containing all of the tweets found in real time. Each tweet is stored in datatype dictionary
    of the following format: 

    curr_tweet_dic = {
            "time_stamp": time_stamp, 
            "tweet_id": tweet_id, 
            "tweet_message": tweet_message_notextended, 
            "full_tweet_message": extended_text,
            "user_id": user_id, 
            "user_name": user_name, 
            "user_screen_name": user_screen_name, 
            "replying_to_tweet_id": replying_to_tweet_id,
            "replying_to_user_id": replying_to_user_id, 
            "replying_to_user_screen_name": replying_to_user_screen_name
        }

    data 
    curr_tweet_dic.get("full_tweet_message") 
    Call the functions accordingly. 

4. Use member functions of class HeavensDoor from twitterBotTool.py to interact with twitter using HebunzADoA twitter
   handle. Functions include but are not limited to, tweeting (status update), replying to tweets (status update), 
   retweet, follow, and getting a userID and their Screen Name (this function isn't that useful..). 

5. Use a loop to continually update and check tweepyListener.continuous_tweets member variable for new tweets.  
'''
def main(keywords=['jetblue']):

    # Initialize twitterBotTool class 
    tool = tbtool.HeavensDoor("pQ9HyAWJfLFcNLnAfKwRE168p", "WncblPIWdsLQIl7pNjy9MqLlGYHAparajjH65jPYhivQzbdeDg",
            "1187900179883679745-g63YFJ07goNk6ntP9S807GZw2RfOUs", "cZXX56mcGffFwhr8bV7R7SIrPrQprfauEhzmvwNnn1psd")

    tl.main(keywords)  

    '''
    The while loop to refresh tweets from tl.continuous_tweets is ultimately
    redundant as you can just reference tl.continuous_tweets
    '''
    while(True):

        # Give delay so program is not continuously refreshing  
        time.sleep(1) 

        if len(tweets) != len(tl.continuous_tweets): 
            tweets = tl.continuous_tweets  
            print(tweets, "\n\n") 

        

if __name__ == "__main__": 
    main() 


