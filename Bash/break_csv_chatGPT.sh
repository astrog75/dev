#!/bin/bash

# Check if correct number of arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <input_file.csv> <number_of_pieces>"
    exit 1
fi

input_file=$1
k=$2

# Check if the file exists
if [ ! -f "$input_file" ]; then
    echo "File not found: $input_file"
    exit 1
fi

# Get the total number of lines in the CSV file
total_lines=$(wc -l < "$input_file")

# Calculate the number of lines per piece
lines_per_piece=$((total_lines / k))
remainder=$((total_lines % k))

# Header of the CSV file (first line)
header=$(head -n 1 "$input_file")

# Function to split the CSV file into k pieces
split_csv() {
    local start_line=2  # Start after the header
    for i in $(seq 1 $k); do
        # Determine the number of lines for the current piece
        if [ $i -le $remainder ]; then
            lines_for_piece=$((lines_per_piece + 1))
        else
            lines_for_piece=$lines_per_piece
        fi
        
        # Create the output file name
        output_file="output_part_$i.csv"

        # Write the header to the output file
        echo "$header" > "$output_file"

        # Extract the lines for the current piece
        sed -n "${start_line},$((start_line + lines_for_piece - 1))p" "$input_file" >> "$output_file"

        # Update the start line for the next piece
        start_line=$((start_line + lines_for_piece))
    done
}

# Call the function to split the CSV
split_csv

echo "CSV file has been split into $k pieces."
