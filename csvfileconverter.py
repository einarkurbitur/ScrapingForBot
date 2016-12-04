import csv

outtext = ""

with open('SpaceX_tweets.csv') as f:
     reader = csv.DictReader(f)
     for row in reader:
         print( row['text'] + ".")
