# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import csv

# Instantiates a client
client = language.LanguageServiceClient()


"""
This script Reads data from Processed Reddit data.
It gets the sentiment value of the Reddit Post + Body using Google Cloud's NLP tool.
It then puts it into a csv file for presentation.
"""


def getSentiment(input):
    document = types.Document(
        content=input,
        type=enums.Document.Type.PLAIN_TEXT)
    try:
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        return [sentiment.score, sentiment.magnitude]
    except:
        return -1


def appendToCSV(TimeStamp, Sentiment, Emphasis):
    with open("RedditUnitedAirlinesAnalysis.csv", mode='a') as csv_file:
        fieldnames = ['tweetID', 'TimeStamp', 'Text', 'Sentiment', 'Emphasis']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(
            {'tweetID': '', 'TimeStamp': TimeStamp, 'Text': '', 'Sentiment': Sentiment, 'Emphasis': Emphasis})


with open('UnitedAirlinesReddit.csv', 'r', encoding='utf8', errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 1
    for row in csv_reader:
        if line_count == 1:
            with open("RedditUnitedAirlinesAnalysis.csv", mode='w') as csv_file:
                fieldnames = ['tweetID', 'TimeStamp', 'Text', 'Sentiment', 'Emphasis']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
            line_count += 1

        else:
            text = row[1] + row[2]
            print(text)
            # Added to CSV file of sentiment values
            if (row[1] != "Delta"):
                document = types.Document(
                    content=text,
                    type=enums.Document.Type.PLAIN_TEXT)
                try:
                    sentiment = client.analyze_sentiment(document=document).document_sentiment
                    appendToCSV(row[0], sentiment.score, sentiment.magnitude)
                except:
                    pass
            line_count += 1
    print(f'Processed {line_count} lines.')
