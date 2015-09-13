#!/usr/bin/env python

from twitter import Twitter
from twitter import OAuth
import json
import argparse
import ConfigParser

def auth():
    parser = ConfigParser.ConfigParser()
    parser.read('config.ini')
    
    OAUTH_TOKEN = parser.get('twitter', 'OAUTH_TOKEN') 
    OAUTH_SECRET = parser.get('twitter', 'OAUTH_SECRET')
    CONSUMER_KEY = parser.get('twitter', 'CONSUMER_KEY')
    CONSUMER_SECRET = parser.get('twitter', 'CONSUMER_SECRET')
    print "[+] Authenticating..."
    try:
        t = Twitter(
                    auth=OAuth(
                               OAUTH_TOKEN, 
                               OAUTH_SECRET, 
                               CONSUMER_KEY, 
                               CONSUMER_SECRET
                              )
                   )
        print "[+] Authentication Succesful!"
        return t
    except Exception, e:
        print "[!] Error authentcating: ", e
        exit()


def main():
    twitter = auth()
    tweets = []
    response = twitter.statuses.user_timeline(
                                              screen_name="botorama2", 
                                              count=10)
    tweets = []

    for i in range(0, len(response)):
        if response[i]['place'] is None:
            location = 'NA'
        else:
            location = response[i]['place']['full_name']
        if response[i]['created_at'] is None:
            date = 'NA'
        else:
            date = response[i]['created_at']
        if response[i]['text'] is None:
            tweet = 'NA'
        else:
            tweet = response[i]['text']

        tweets.append({'username':'botorama2',
                       'tweet':tweet,
                       'date':date,
                       'location':location})

    for tweet in tweets:
        print tweet

if __name__ == '__main__':
    main()
