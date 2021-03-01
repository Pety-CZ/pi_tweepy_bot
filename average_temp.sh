#!/bin/sh

#grep 'temperature' /var/mail/pi | tail -n18 | cut -d' ' -f5 | cut -c1-4 | awk 'BEGIN{pocet=0;soucet=0} {pocet+=1;soucet+=$1} END{printf "%dC\n", soucet/pocet}'
grep 'temperature' /var/mail/pi | cut -d' ' -f5 | tr -d '\n' | tr 'C' '\n' | tr -d ".\'" |  awk 'BEGIN{pocet=0;soucet=0} {pocet+=1;soucet+=$1} END{printf "%f°C\n", soucet/pocet/10}' >> temp.txt
