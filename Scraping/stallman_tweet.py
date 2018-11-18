# tweet Free as in Freedom
# by Richard Stallman
# am sure he does not approve of Twitter
# see: https://stallman.org/twitter.html
# added a random piece to the frequency of tweets
# hopefully trying to keep from becoming a spammer

import tweepy
from random import randint
from time import sleep
from API_KEYS import TWITTER_CONSUMER
from API_KEYS import TWITTER_CONSUMER_SECRET
from API_KEYS import TWITTER_ACCESS
from API_KEYS import TWITTER_ACCESS_SECRET

# keys
consumer_key = TWITTER_CONSUMER
consumer_secret = TWITTER_CONSUMER_SECRET
access_token = TWITTER_ACCESS
access_token_secret = TWITTER_ACCESS_SECRET

# authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# open stallman file
stallman_file = open('free_as_in_freedom.txt', 'r')
file_lines = stallman_file.readlines()
stallman_file.close()

# iterate through document
for line in file_lines:
    try:
        print(line)
        if line != '\n':
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(randint(600,3600))
