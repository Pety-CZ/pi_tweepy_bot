#!/usr/bin/env python
import sys
import tweepy
import random


# loads APIs needed for authorization
f = open("/home/pi/Bot/CONSUMER_KEY.txt", "r")
CONSUMER_KEY = f.read()
f.close()

f = open("/home/pi/Bot/CONSUMER_SECRET.txt", "r")
CONSUMER_SECRET = f.read()
f.close()

f = open("/home/pi/Bot/ACCES_TOKEN.txt", "r")
ACCES_TOKEN = f.read()
f.close()

f = open("/home/pi/Bot/ACCESS_TOKEN_SECRET.txt", "r")
ACCESS_TOKEN_SECRET = f.read()
f.close()

# authentication with APIs
auth = tweepy.OAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
auth.set_access_token('ACCES_TOKEN', 'ACCESS_TOKEN_SECRET')
api = tweepy.API(auth)


f = open("USER.txt", "r")
USER = f.read()
f.close()

# BOT will get number of its followers
user = api.get_user('USER')
followers = user.followers_count
followers = 'number of my followers is ' + str(followers)

# BOT will follow all its followers
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

# BOT will randomly select one mood from list bellow
moods = ["happy", "sad", "angry", "tense", "hopeful", "lonely", "amused", "calm", "friendly", "energetic", "optimistic", "pessimistic", "flirty", "annoyed", "depressed", "rejected", "restless", "irritated", "sleepy"]

mood_num = len(moods) - 1
bot_mood = moods[random.randint(0, mood_num)]
bot_mood = 'I feel ' + bot_mood

# get system data from bash outpus
f = open("data.txt", "r")
bash = f.read()
f.close()

# All data is put into one final string
tweet = str(bash) + str(bot_mood) + ' and ' + str(followers) + '.\n' + '#raspberrypi ' +  '#bot'

# Tweet wil be tweeted
api.update_status(status=tweet)

# displays tweeted tweet
print "---------------------TWEETED--------------------\n" + data
