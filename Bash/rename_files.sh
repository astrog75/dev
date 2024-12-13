#!/bin/bash
# This script renames all files containing a whitespace in its name, 
# in the current directory

for fname in *
do
	echo "$fname" | grep -q ' '
	if [ $? -eq 0 ]
	then
        new_fname=`echo $fname | sed -e "s/ /_/g"`
        echo $new_fname
        mv "$fname" "$new_fname"
	fi
done
