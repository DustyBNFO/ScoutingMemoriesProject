#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:30:11 2024

@author: dustyzeliff
"""
import csv

# Define the paths to your CSV files
final_updated_councils_csv_path = 'final_updated_councils_2.csv'
council_groups_csv_path = 'CouncilGroups.csv'
output_csv_path = 'new_final_updated_councils.csv'

# Create a dictionary from CouncilGroups.csv with keys from column 1 and values from column 2
council_group_dict = {}
with open(council_groups_csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        if len(row) > 1:
            key = row[0].strip()
            print(key)
            value = row[1].strip()
            council_group_dict[key] = value
print(council_group_dict)
# Read final_updated_councils_2.csv and process each row
with open(final_updated_councils_csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)
    header = rows[0]  # Extract header
    rows = rows[1:]  # Extract data rows

# Add a new column for the match results
header.append('CouncilGroup')
updated_rows = [header]

# Process each row
for row in rows:
    if len(row) > 2:  # Ensure there are enough columns in the row
        formatted_council_name = row[2].strip()  # "FormattedCouncilName" is the 3rd column (index 2)
        matched_entry = council_group_dict.get(formatted_council_name, '')
        row.append(matched_entry)  # Append the matching entry or an empty string if no match found
        updated_rows.append(row)
    else:
        print(f"Skipping row due to insufficient columns: {row}")

# Write the updated rows to a new CSV file
with open(output_csv_path, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(updated_rows)

print(f"The data has been updated and written to '{output_csv_path}' with matching entries.")

