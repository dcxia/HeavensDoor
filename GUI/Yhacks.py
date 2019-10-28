#%%
import csv
import statistics as s



data = dict()

mean = s.mean(values)
stdev = s.stdev(values)

def putInData(data,key,sentiment):
   # ranges are -1 to -0.5 to 0 to 0.5 to 1
   if key not in data:
       data[key] = [0,0,0,0]
   else:
       if sentiment > mean + (1.75*stdev):
           data[key][3] += 1
       elif sentiment > mean + (0.5*stdev):
           data[key][2] += 1
       elif sentiment > mean - (0.5*stdev):
           pass
            #data[key][2] += 1 neutral
       elif sentiment > mean - (1.75*stdev):
           data[key][1] += 1
       else:
           data[key][0] += 1

values =[]

with open("C:/Users/nucle/Documents/Python Scripts/RedditUnitedAirlinesAnalysis.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter =',')
    row_number = 0
    for row in readCSV:
        if row_number > 1 and (row_number % 2 == 0):
            date = row[1][0:4]
            val = float(row[3]) * float(row[4])
            values.append(val)
            putInData(data,date,val)
        row_number+=1






#%%
for keys in data.keys():
    senti_sum = sum(data[keys])
    for i in range(len(data[keys])):
        data[keys][i] = (data[keys][i]/senti_sum) * 100

#%%
del data['2014']
del data['2013']
del data['2012']
del data['2011']
del data['2010']
del data['2009']
#del data['2008']

#%%


#%%
keys = []
values = []
sentiment = []

senti_list = ["Very Negative", "Negative", "Positive", "Very Positive"]
for key in data.keys():
    for i in range(len(data[key])):
        keys.append(key)
        sentiment.append(senti_list[i])
        values.append(data[key][i])

#%%
import pandas as pd

list_of_tuples = list(zip(sentiment, keys, values))  

df = pd.DataFrame(list_of_tuples, columns = ['Sentiment', 'Keys', 'Senti_Values'])
df["Rank"] = df.groupby("Keys")["Senti_Values"].rank("first", ascending=False)

df = df.sort_values(by=['Keys'])

#%%
df.to_csv(r'C:/Users/nucle/Desktop/TestData2.csv')

