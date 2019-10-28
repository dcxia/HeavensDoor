# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import csv

"""
This script Reads data from Processed Twitter data.
It gets the sentiment value of the twitter tweet using Google Cloud's NLP tool.
It then puts it into a csv file for presentation.
"""



# Instantiates a client
client = language.LanguageServiceClient()

def appendToCSV(tweetID,TimeStamp,Text, Sentiment,Emphasis):
    with open("TwitterDeltaAnalysis.csv", mode ='a') as csv_file:
        fieldnames = ['tweetID', 'TimeStamp', 'Text','Sentiment','Emphasis']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'tweetID': tweetID, 'TimeStamp': TimeStamp, 'Text': '','Sentiment': Sentiment,'Emphasis': Emphasis})

with open('RedditDelta.csv', 'r', encoding='utf8', errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            with open("TwitterDeltaAnalysis.csv", mode='w') as csv_file:
                fieldnames = ['tweetID', 'TimeStamp', 'Text', 'Sentiment', 'Emphasis']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        else:
            print(f'\t Tweet ID: {row[0]} \t Time Stamp: {row[1]} \t Text: {row[2]}.')
            text = row[2]

            #Added to CSV file of sentiment values
            if (row[1] != "Delta"):
                document = types.Document(
                    content=text,
                    type = enums.Document.Type.PLAIN_TEXT)
                try:
                    sentiment = client.analyze_sentiment(document=document).document_sentiment
                    appendToCSV(row[0], row[1], row[2], sentiment.score, sentiment.magnitude)
                except:
                    pass
            line_count += 1
    print(f'Processed {line_count} lines.')
