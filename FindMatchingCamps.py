#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:26:25 2025

@author: dustyzeliff
"""
import pandas as pd
import re

# Read the CSV files into DataFrames with a specific encoding and low_memory=False
camps_df = pd.read_csv('Camps-Large list.csv', encoding='ISO-8859-1', low_memory=False)
known_camps_df = pd.read_csv('CampNamesKnown.csv', encoding='ISO-8859-1')

# Limit to the first 12124 rows
camps_df = camps_df.iloc[:12124]

# Extract the fifth column from Camps-Large list
camp_names = camps_df.iloc[:, 4].fillna('')  # Replace NaN with empty string

# Remove the word "camp" from the entries in CampNamesKnown.csv
def remove_camp_from_string(s):
    return re.sub(r'(?i)\bcamp\b', '', s)

known_camp_names = [remove_camp_from_string(name) for name in known_camps_df.values.flatten()]

# Function to find the most similar match with a minimum length of 5 characters
def find_most_similar(entry, known_camp_names):
    entry = str(entry)  # Ensure entry is a string
    excluded_strings = ['camp', 'name']
    best_match = ('no match', 0)  # Initialize best match and similarity ratio
    for i in range(len(entry) - 4):  # Loop through entry for substrings of length 5 or more
        substring = entry[i:i+5]
        # Exclude substrings containing "Camp", "camp", "Name", or "name"
        if any(excluded_str in substring.lower() for excluded_str in excluded_strings):
            continue
        for known_camp in known_camp_names:
            if substring in known_camp:
                return known_camp  # Return the matching entry
    return 'no match'

# List to store matching results
matches = []

# Iterate through the 5th column entries
for camp_name in camp_names:
    match = find_most_similar(camp_name, known_camp_names)
    matches.append(match)

# Add the match results as a new column to the DataFrame at the 19th position
camps_df.insert(18, 'Match', matches)

# Save the DataFrame to a new CSV file
camps_df.to_csv('Camps-Large list with Matches.csv', index=False)

print("New CSV file with matches created successfully!")

