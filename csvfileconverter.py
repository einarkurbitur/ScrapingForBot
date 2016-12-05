import csv
from TextFixer import filter_tweet

outtext = ""

with open('SpaceX_tweets.csv') as f:
     reader = csv.DictReader(f)
     for row in reader:
         outtext += filter_tweet(row['text']) + ".\n"

with open('spacex_out.txt', 'w') as f:
     f.write(outtext)
