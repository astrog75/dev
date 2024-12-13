#!/bin/bash

# Print number of regular unhidden files, directories and executables 
# in directory given in input
# If no directory is provided, the script operates on the current directory

if (( $# == 0 )); then
	wd=$(pwd)
elif (( $# == 1 )); then
	wd=$1
else
	echo "Invalid number of parameters"
	exit 1
fi

nb_files=$(ls -l $wd | grep ^- | wc -l)
nb_dir=$(ls -l $wd | grep ^d | wc -l)
nb_exec=$(ls -l $wd | grep ^x | wc -l)

echo "$wd contains $nb_files regular unhidden files,\
 $nb_dir directories and $nb_exec executables"
