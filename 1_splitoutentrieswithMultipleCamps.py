#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:54:03 2024

@author: dustyzeliff
"""

import csv

# Define the path to your input and output CSV files
input_csv_path = 'AllCampsJoin.csv'  # Replace with your actual input file name
output_csv_path = 'expanded_scout_camps.csv'  # The output file name

# Read the input CSV file and process each row
with open(input_csv_path, mode='r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Read the header row
    expanded_rows = [header]  # Initialize with header row

    # Process each row
    for row in reader:
        council_ids = row[3].split(', ')  # Split the council_id column by comma and space
        council_names = row[4].split(', ')  # Split the council_name column by comma and space

        # Ensure the number of council_ids matches the number of council_names
        if len(council_ids) != len(council_names):
            print(f"Warning: Mismatch in council IDs and names in row: {row}")
            expanded_rows.append(row)
            continue  # Skip this row

        # Create a new row for each council_id and council_name
        for i in range(len(council_ids)):
            new_row = row[:3] + [council_ids[i]] + [council_names[i]]
            expanded_rows.append(new_row)

# Write the expanded rows to the output CSV file
with open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(expanded_rows)

print(f"The expanded data has been written to '{output_csv_path}'.")
