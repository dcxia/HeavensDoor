#%%
from tkinter import *
import tkinter as tk
import tweepyListener as tl 
import twitterBotTool as tbl
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import imageio
from PIL import Image, ImageTk
from pathlib import Path

import os
folderpath = os.getcwd()

keywords = [] 

tool = tbl.HeavensDoor()

class MADEINHEAVEN: 

    def __init__(self): 

        window = tk.Tk() # Create a window 
        window.title("YHacks: Heaven's Door") # Set title 

        Button(window, text = "View Graphs!", width = 25, height = 15, 
                                command = self.view_graphs).grid( 
                                row = 2, column = 1, sticky = W)

        Button(window, text = "View Live Tweets!", width = 25, height = 15, 
                                command = self.LiveTweets).grid( 
                                row = 2, column = 2, sticky = E)

        window.mainloop()  # Create event loop

    def view_graphs(self):

        window = Toplevel() # Create a sub-window 
        window.title("Graph Viewer") # Set title

        self.t_JetBlue_var = IntVar()
        self.t_United_var = IntVar()
        self.t_Delta_var = IntVar()

        self.r_JetBlue_var = IntVar()
        self.r_United_var = IntVar()
        self.r_Delta_var = IntVar()

        Label(window, text = "Choose your graphs (Check only one side)").grid(row = 0, 
                                          column = 2, sticky = W)
        Label(window, text = "Twitter Graphs").grid(row = 1, 
                                          column = 1, sticky = W)
        Label(window, text = "Reddit Graphs").grid(row = 1, 
                                          column = 3, sticky = W)                                    
        
        Checkbutton(window, text='JetBlue', variable=self.t_JetBlue_var).grid(
                                            row=2, column=1, sticky=W) 
        Checkbutton(window, text='United Airlines', variable=self.t_United_var).grid(
                                            row=3, column=1, sticky=W)
        Checkbutton(window, text='Delta', variable=self.t_Delta_var).grid(
                                            row=4, column=1, sticky=W) 

        Checkbutton(window, text='JetBlue', variable=self.r_JetBlue_var).grid(
                                            row=2, column=3, sticky=W) 
        Checkbutton(window, text='United Airway', variable=self.r_United_var).grid(
                                            row=3, column=3, sticky=W)
        Checkbutton(window, text='Delta', variable=self.r_Delta_var).grid(
                                            row=4, column=3, sticky=W)

        Button(window, text = "Show Graphs", 
                                command = self.GraphButton).grid( 
                                row = 5, column = 2)

    def GraphButton(self):
        
        def stream(label):
        
            try:
                image = video.get_next_data()
            except:
                video.close()
                return
            label.after(delay, lambda: stream(label))
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image

        TJet = self.t_JetBlue_var.get()
        TUni = self.t_United_var.get()
        TDel = self.t_Delta_var.get()

        RJet = self.r_JetBlue_var.get()
        RUni = self.r_United_var.get()
        RDel = self.r_Delta_var.get()

        if TJet and TUni and TDel == 1:
            video_name = str(folderpath)+"/UJD_Twitter.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif TJet and TUni == 1:
            video_name = str(folderpath)+"/UJ_Twitter.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif TUni and TDel == 1:
            video_name = str(folderpath)+"/UD_Twitter.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif TJet and TDel == 1:
            video_name = str(folderpath)+"/JD_Twitter.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif TJet == 1:
            video_name = str(folderpath)+"/J_Twitter.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif TUni == 1:
            video_name = str(folderpath)+"/U_Twitter.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif TDel == 1:
            video_name = str(folderpath)+"/D_Twitter.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif RJet and RUni and RDel == 1:
            video_name = str(folderpath)+"/UJD.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif RJet and RUni == 1:
            video_name = str(folderpath)+"/UJ_Reddit.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif RUni and RDel == 1:
            video_name = str(folderpath)+"/UD_Reddit.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif RJet and RDel == 1:
            video_name = str(folderpath)+"/JD_Reddit.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif RJet == 1:
            video_name = str(folderpath)+"/J_Reddit.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif RUni == 1:
            video_name = str(folderpath)+"/U_Reddit.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        elif RDel == 1:
            video_name = str(folderpath)+"/D_Reddit.mp4"
            
            video = imageio.get_reader(video_name)
            delay = int(1000 / video.get_meta_data()['fps'])
            root = Toplevel()
            my_label = Label(root)
            my_label.pack()
            my_label.after(delay, lambda: stream(my_label))
            root.mainloop()

        else: 
            print("Please choose a valid combination")


    def LiveTweets(self):

        window = Toplevel() # Create a sub-window 
        window.title("Live Tweet Window") # Set title

        Label(window, text = "Type keyword here:").grid(row = 1, 
                                          column = 2)

        self.keyword = StringVar()  
        Entry(window, textvariable = self.keyword, 
                    justify = RIGHT).grid(row = 2, column = 2) 
        Button(window, text = "Enter Keyword", 
                                command = self.EnterKeyword).grid( 
                                row = 2, column = 3)

    
    def EnterKeyword(self):

        window = Toplevel() # Create a sub-window 
        window.title("Tweet Viewer") # Set title

        keyword = self.keyword.get()

        keywords = keyword.split(",") 
        # print(keywords)
        # print(keyword)

        tl.main(keywords)
        print(keywords)
        tweet = StringVar()
        Senti_str = StringVar()
        Confi_str = StringVar()

        # Instantiates a client
        client = language.LanguageServiceClient()

        def getSentiment(input):
            document = types.Document(
                content=input,
                type=enums.Document.Type.PLAIN_TEXT)
            try:
                sentiment = client.analyze_sentiment(document=document).document_sentiment
                print("Succesfully Got sentiment")
                return [sentiment.score, sentiment.magnitude]
            except:
                return -1


        def Refresh():
            if len(tl.continuous_tweets) > 0: 
                tweets = tl.continuous_tweets[-1].get("full_tweet_message")
                #Todo Put in sentiment model here.
                sentiment = getSentiment(tweets)
                Senti_str.set(sentiment[0])
                Confi_str.set(sentiment[1])
                print(tweets)
                tweet.set(tweets)

        Label(window, textvariable = tweet, font=("Helvetica", 10)).grid(row = 3, 
            column = 2)
        Label(window, textvariable = Senti_str).grid(row = 4, 
            column = 5)
        Label(window, textvariable = Confi_str).grid(row = 5,
            column = 5)

        def Retweet():
            tweet_id = tl.continuous_tweets[-1].get("tweet_id")
            tool.retweet(tweet_id)


        Label(window, text = "Live Tweet Viewer").grid(row = 0, 
                                          column = 2)

        Label(window, text = "Sentiment:").grid(row = 4, 
                                    column = 2)
        Label(window, text = "Confidence:").grid(row = 5, 
                                    column = 2)


        Button(window, text = "Refresh", 
                                command = Refresh).grid( 
                                row = 8, column = 2)  
     
        Button(window, text = "Retweet", 
                                command = Retweet).grid( 
                                row = 8, column = 1)

        Button(window, text = "Respond", 
                                command = self.Respond).grid( 
                                row = 8, column = 3)


    def Respond(self):

        window = Toplevel() # Create a sub-window 
        window.title("Response Window") # Set title

        Label(window, text = "Type response here:").grid(row = 0, 
                                          column = 2, sticky = W)
        self.Res_str = StringVar()  
        Entry(window, textvariable = self.Res_str, 
                    justify = RIGHT).grid(row = 2, column = 2) 
    
        Button(window, text = "Send", 
                                command = self.SendResponse).grid( 
                                row = 3, column = 2)

    def SendResponse(self):
        tweet_id = tl.continuous_tweets[-1].get("tweet_id")
        user_screen_name = tl.continuous_tweets[-1].get("user_screen_name")
        res_str = self.Res_str.get()
        print(res_str)

        tool.reply_tweet(res_str, tweet_id, user_screen_name)
        #tbl.reply_tweet(res_str, tweet_id)




    def placeholder(self):
        print("hi")

    

MADEINHEAVEN()