#!/bin/sh
#uname -a | cut -d' ' -f3 > kernel.txt

echo "$(/opt/vc/bin/vcgencmd measure_temp)" | cut -c6- > /home/pi/Bot/pi_temp.txt
echo "Current time in Benešov is $(date -d '+1 hour' '+%H : %M : %S, %N').\n" \
 > /home/pi/Bot/data_daily.txt | python /home/pi/Bot/bot_tweet_daily.py
