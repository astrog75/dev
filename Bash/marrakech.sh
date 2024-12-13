#!/bin/bash

while read -r line
do
	for w in $line
	do
		echo "$w" >> file_broke_down.txt
	done
done < accroches.txt

content=$(sort file_broke_down.txt | uniq -c | sort)
echo "$content"
echo $(echo "$content" | tail -n 3 | head)
