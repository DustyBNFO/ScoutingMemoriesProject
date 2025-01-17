#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:56:29 2024

@author: dustyzeliff
"""
import csv
import re


#simple script to compare to columns in a csv and determine if there is matching text
#from the first column in the 2nd column. The regex is currently used to find
#the string before the - character, as this is checking council names. 


with open('councils_us_csv_for_spot_check.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)  
    header = next(reader)
    matches = []
    pattern = re.compile(r'^(.*?)-')

    for row in reader:
        first_column_value = row[1]
        

        match = pattern.search(first_column_value)
        
        if match:
            # Extract the value, remove spaces, and convert to lowercase
            extracted_value = match.group(1).replace(' ', '').lower()
            column_13_value = row[14]
            print(extracted_value)
            column_13_value = row[14]
            print(column_13_value)
           
            if extracted_value in column_13_value:
                matches.append("True")
            else:
                matches.append("False")



print(matches)


