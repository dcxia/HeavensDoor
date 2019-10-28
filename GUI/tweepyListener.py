import tweepy
from tweepy import Stream
import pandas as pd
import twitterBotTool

# Import google cloud sentiments API library:
# import sentimentsCalculator as sc

# global variable keeping track of continuous tweets...
continuous_tweets = []


# override tweepy.StreamListener to add logic to on_status, on_data and on_error
class MyStreamListener(tweepy.StreamListener):

    # def on_status(self, status):
    #     print(status.text)

    # Fix extended tweeting errors
    def on_status(self, status):
        try:
            if hasattr(status, 'retweeted_status') and hasattr(status.retweeted_status, 'extended_tweet'):
                extended_text = 'retweeted: ' + status.retweeted_status.extended_tweet['full_text']
                print(extended_text)
            if hasattr(status, 'extended_tweet'):
                extended_text = 'extended_tweet: ' + status.extended_tweet['full_text']
                print(extended_text)
            else:
                extended_text = status.text
                print('text: ' + status.text)
        except AttributeError:
            extended_text = 'attribute error: ' + status.text
            print(extended_text)

        print("Metadata...\n\n")
        print(status)
        # print(status)
        time_stamp = status.created_at
        tweet_id = status.id_str
        tweet_message_notextended = status.text

        user_id = status.user.id_str
        user_name = status.user.name
        user_screen_name = status.user.screen_name

        # useless stuff we don't need now
        replying_to_tweet_id = status.in_reply_to_status_id_str
        replying_to_user_id = status.in_reply_to_status_id_str
        replying_to_user_screen_name = status.in_reply_to_screen_name

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

        continuous_tweets.append(curr_tweet_dic)

        print("\n\nPreviously saved tweets...\n\n{}\n\n".format(continuous_tweets))
        print("\n\nCurrent Tweet: {}\n\n".format(curr_tweet_dic))

    # def on_data(self, data):

    #     # We want 6 things
    #     # 1. Time stamp
    #     # 2. Tweet ID
    #     # 3. Tweet message
    #     # 4. User ID
    #     # 5. User Twitter Handle
    #     # 6. User Twitter Screen Name

    #     curr_tweet = []

    #     time_stamp = data

    #     '''
    #     STUPID METHOD OF REFERENCING STATIC OBJECT MEMBER VARIABLES...
    #     A memo by Irenaeus Wong October 26th 2019 3:01pm.

    #     # Append time stamp
    #     start = tweet_data.find("created_at") + 12
    #     end = tweet_data.find("id") - 5
    #     time_stamp = tweet_data[start:end].strip("\"")
    #     curr_tweet.append(time_stamp)

    #     # Append tweet id:
    #     start = tweet_data.find("id_str") + 8
    #     end = tweet_data.find("text") - 3
    #     tweet_id = tweet_data[start:end].strip("\"")
    #     curr_tweet.append(tweet_id)

    #     # Append the actual tweet
    #     message_start_index = tweet_data.find("text") + 7
    #     message_end_index = tweet_data.find("source") - 2
    #     tweet_message = tweet_data[message_start_index:message_end_index].strip("\"")
    #     curr_tweet.append(tweet_message)

    #     # Append User id
    #     start = tweet_data.find("\"user\":{") + 13
    #     substring = tweet_data[start:]
    #     user_id = substring.split(",")[0]
    #     user_id = user_id.strip("\"")
    #     curr_tweet.append(user_id)

    #     # Append user twitter handle
    #     start = tweet_data.find("\"name\":") + 8
    #     end = tweet_data.find("\"screen_name\":") - 2
    #     twitter_handle = tweet_data[start:end]
    #     curr_tweet.append(twitter_handle)

    #     continuous_tweets.append(curr_tweet)

    #     '''
    #     # print("\n\n\nAll Tweets so far...\n\n{}".format(continuous_tweets))
    #     # print("Current Tweet Data:{}".format(curr_tweet))

    #     # Increment curr_tweet_num to trigger computations and actions:
    #     # curr_tweet_num += 1

    #     return True

    def on_error(self, status_code):
        if status_code == 420:
            # Returning false in on_error disconnects the stream
            return True


if __name__ == "__main__":
    main("jetblue")


def main(keywords):
    # Initialize keys for authentication...
    consumer_key = "pQ9HyAWJfLFcNLnAfKwRE168p"
    consumer_secrete = "WncblPIWdsLQIl7pNjy9MqLlGYHAparajjH65jPYhivQzbdeDg"
    access_token = "1187900179883679745-g63YFJ07goNk6ntP9S807GZw2RfOUs"
    access_token_secrete = "cZXX56mcGffFwhr8bV7R7SIrPrQprfauEhzmvwNnn1psd"
    # create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secrete)
    auth.set_access_token(access_token, access_token_secrete)

    # initialize Tweepy API
    api = tweepy.API(auth)

    # Creating a stream
    # api with valid authentication created earlier
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, tweet_mode='extended')

    # Starting a stream:
    # Use filter stream to stream all tweets containing the word 'jet', 'blue', and 'jetblue'
    myStream.filter(track=keywords, is_async=True)

    # prev_tweet_num = 0

    # # Variable controlling if a very bad rating is found with decent confidence
    # raise_negative_notif = False
    # raise_positive_notif = False

    # # initialze twitterbot toolbox as object
    # tt = twitterBotTool.HeavensDoor()

    # while(True):

    #     if prev_tweet_num < curr_tweet_num:

    #         # Process tweet message if it exceeds 150 characters.
    #         if len(tweet_message) > 150:
    #             tweet_message = tweet_message[0:151]

    #         curr_sentiments, curr_confidence = sc.getSentiments(tweet_message)

    #         # Sentiment is found. Determine courses of action.
    #         if curr_confidence > 0.5 and curr_sentiments < -0.75:
    #             raise_negative_notif = True
    #         elif curr_confidence > 0.5 and curr_sentiments > 0.75:
    #             raise_positive_notif = True

    #         sendToDjango(raise_positive_notif, raise_negative_notif, tweet_message)
