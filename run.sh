#!/bin/sh
#sh /home/pi/Bot/pripady.sh
echo "$(/opt/vc/bin/vcgencmd measure_temp)" | cut -c6- > /home/pi/Bot/pi_temp.txt
echo "Precise time in London is $(date '+%H : %M : %S, %N').\nMy brain's temperature is $(/opt/vc/bin/vcgencmd measure_temp | cut -c6-11)." > /home/pi/Bot/data.txt | python /home/pi/Bot/bot_tweet.py
