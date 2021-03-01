#!/bin/sh
#sh /home/pi/Bot/pripady.sh
#echo "$(/opt/vc/bin/vcgencmd measure_temp)" | cut -c6- > /home/pi/Bot/pi_temp.txt
echo "Precise time in London is $(date '+%H : %M : %S, %N').\n" > data.txt | python bot_tweet.py
