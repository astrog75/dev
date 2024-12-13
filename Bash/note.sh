#!/bin/bash

sum=0
nb=0

while true;
do
	read -rp "Entrez une note : " note
	if ((note == 0)); then
		break
	fi
	
	sum=$((sum+note))
	nb=$((nb+1))
done

x=$(echo "scale=2;$sum/$nb" | bc)
echo $x

