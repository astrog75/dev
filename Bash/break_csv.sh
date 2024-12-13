#!/bin/bash
#
# Breaks a csv file into smaller parts using "split" command.
#
# Syntax : ./break_csv filename nb_parts
# 
# Each part will have the header of the original file
# If nb_parts is not declared, its default value is 2


# Retrieving the file and the desired nb_parts, if provided
if [[ $# -eq 0 ]]
then
	echo "Please provide a filename"
	exit 1
elif [[ $# -eq 1 ]]
then
	nb_parts=2
else
	nb_parts=$2
fid


# 2. Checking if the file exists and if it's a csv file
filename=$1
if [[ ! -f "$filename" ]]
then
	echo "The provided file doesn't exist in the current directory"
	exit 1
elif [[ "$filename" != *.csv ]]
then
	echo "The provided file is not a csv file"
	exit 1
fi

basename=${filename%.csv}
header=$(head -1 $filename)

# to be continued...
split -d -n "$nb_parts" --additional-suffix=".csv" "$filename" "$basename""_"

echo $(wc -l sample*)

for f in "$basename""_"*
do
	cat "$f" > tmp
	echo "$header" > "$f"
	cat tmp >> "$f"
done

rm tmp
