#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:26:07 2025

@author: dustyzeliff
"""

import pandas as pd

# Load the CSV file
file_path = "new_camp_ids.csv"
df = pd.read_csv(file_path)

# Initialize a dictionary to keep track of duplicates
duplicate_counter = {}

# Function to modify duplicate lines
def modify_duplicate(line):
    if line in duplicate_counter:
        duplicate_counter[line] += 1
        parts = line.split('-')
        parts[0] += str(duplicate_counter[line])
        return '-'.join(parts)
    else:
        duplicate_counter[line] = 1
        return line

# Apply the function to each line in the first column
df['Modified'] = df.iloc[:, 0].apply(modify_duplicate)

# Save the updated dataframe to a new CSV file
updated_file_path = "updated_camp_ids.csv"
df.to_csv(updated_file_path, index=False)

print(f"Duplicates modified and saved to '{updated_file_path}'")
