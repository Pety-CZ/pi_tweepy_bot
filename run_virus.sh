#!/bin/sh
uname -a | cut -d' ' -f3 > kernel.txt
#sh /home/pi/Bot/pripady.sh
echo "Current time is Czech Republic is $(date -d '+1 hour' '+%H : %M : %S, %N').\n"\
 > /home/pi/Bot/data_virus.txt | python /home/pi/Bot/bot_tweet_virus.py
