#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:47:15 2025

@author: dustyzeliff
"""

import csv

def process_entry(entry):
    if '(' in entry:
        parts = entry.split('(', 1)
        first_part = parts[0].rstrip()  # Remove any trailing spaces
        remainder = '(' + parts[1]
        return f"{first_part} Council {remainder}"
    else:
        return f"{entry} Council"


def process_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            new_row = [process_entry(entry) for entry in row]
            writer.writerow(new_row)

# Example usage
input_file = 'CouncilNames.csv'
output_file = 'CouncilNamesOutput.csv'
process_csv(input_file, output_file)
