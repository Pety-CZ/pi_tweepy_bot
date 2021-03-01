#!/bin/sh

# page with Covid-19 informations (CZECH)
wget -q 'https://onemocneni-aktualne.mzcr.cz/covid-19'

# variables to get sensible sentence
pripady=$(grep -A 2 'Aktivní případy' covid-19 | tail -n1 | cut -d'"' -f2)
datum=$(grep -A 7 'Aktivní případy' covid-19 | tail -n1 | cut -c51- | tr -d '&nbsp;' | cut -d'v' -f1)
cas=$(grep -A 7 'Aktivní případy' covid-19 | tail -n1 | cut -d';' -f5 | tr -d '&nbsp' | tr '.' ':')
echo Corfirmed active cases of Covid-19 at $cas $datum in Czech Republic: $pripady. > /home/pi/Bot/vir_check.txt

chmod 644 /home/pi/Bot/vir.txt
stary="/home/pi/Bot/vir.txt"
novy="/home/pi/Bot/vir_check.txt"

# check if number of cases changed, tweet new number if did
if cmp -s "$stary" "$novy"; then
	echo 'Nic nového\n'

else
	echo 'Změna\n'
	mv "$novy" "$stary"
	sh /home/pi/Bot/run_virus.sh
fi

# removes residual files
rm covid*
