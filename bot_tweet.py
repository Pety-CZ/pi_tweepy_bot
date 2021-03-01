#!/usr/bin/env python
import sys
import tweepy
import random

moods = ["happy", "sad", "angry", "tense", "hopeful", "lonely", "amused", "calm", "friendly", "energetic", "optimistic", "pessimistic", "flirty", "annoyed", "depressed", "rejected", "restless", "irritated", "sleepy"]

auth = tweepy.OAuthHandler('zf3vYidk4rqNt05RD9bP3cj6K', 'QCxeXAoUm6T4pVSU4i2BzTkzep7U6UoA9niibyRm52HCPuk0fy')
auth.set_access_token('1353644906594631680-ZdAeiQ5htREUa5jRmXwQpuj5o6D3Q5', 'FOVxHwNynR3IFsIMyBOiESqVc2fOABTdRYU3hVkVkt0of')

api = tweepy.API(auth)


#get bot followers
user = api.get_user('Raspberrypi3b2')
followers = user.followers_count
followers = 'number of my followers is ' + str(followers)

#follow followers
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

#mood
mood_num = len(moods) - 1
bot_mood = moods[random.randint(0, mood_num)]
bot_mood = 'I feel ' + bot_mood

#with open('data_6h.txt', 'r') as file:
#	f = file.read()
f = open("/home/pi/Bot/data.txt", "r")
bash = f.read()
f.close()


data = str(bash) + str(bot_mood) + ' and ' + str(followers) + '.\n' + '#raspberrypi ' +  '#bot'

api.update_status(status=data)

print "---------------------TWEETED--------------------\n" + data
