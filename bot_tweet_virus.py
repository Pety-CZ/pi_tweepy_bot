#!/usr/bin/env python
import sys
import tweepy
import random

moods = ["happy", "sad", "angry", "tense", "hopeful", "lonely", "amused", "calm", "friendly", "energetic", "optimistic", "pessimistic", "flirty", "annoyed", "depressed", "rejected", "restless", "irritated", "sleepy"]


auth = tweepy.OAuthHandler('zf3vYidk4rqNt05RD9bP3cj6K', 'QCxeXAoUm6T4pVSU4i2BzTkzep7U6UoA9niibyRm52HCPuk0fy')
auth.set_access_token('1353644906594631680-ZdAeiQ5htREUa5jRmXwQpuj5o6D3Q5', 'FOVxHwNynR3IFsIMyBOiESqVc2fOABTdRYU3hVkVkt0of')

api = tweepy.API(auth)


#get bot followers
#user = api.get_user('Raspberrypi3b2')
#followers = user.followers_count
#followers = 'Number of followers: ' + str(followers)

#follow followers
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()


#creator followers
#user = api.get_user('novak_petr007')
#creator = user.followers_count
#creator = 'Number of followers of my creator: ' + str(creator)


#mood
#mood_num = len(moods) - 1
#bot_mood = moods[random.randint(0, mood_num)]
#bot_mood = 'My mood is ' + bot_mood 

#kernel
#ker = open('/home/pi/Bot/kernel.txt', 'r')
#kernel = ker.read()
#ker.close()
#kernel = ' and my kernel version is ' + str(kernel)

#data
fi = open('/home/pi/Bot/data_virus.txt', 'r')
f = fi.read()
fi.close()

#lucky number
#luckyNumber = random.randint(100000, 999999)
#luckyNumber = "I think today's lucky number is " + str(luckyNumber) + "."

#COVID-19
cov = open("/home/pi/Bot/vir.txt", "r")
covid = cov.read()
cov.close()

data = str(f) + str(covid)
#data = str(f) + str(covid) + str(followers) + '. ' + str(creator) + '.\n' + str(bot_mood) + '.\n' + str(luckyNumber)

api.update_status(status=data)

print "---------------------TWEETED--------------------\n" + data 

