#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:09:34 2025

@author: dustyzeliff
"""

import pandas as pd

# Load the two CSV files
file1 = "pre_changes.csv"
file2 = "post_changes.csv"


df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Add a column to identify the source of each row
df1['source'] = 'file1'
df2['source'] = 'file2'

# Concatenate the dataframes
df_all = pd.concat([df1, df2], ignore_index=True)

# Drop duplicate rows
df_unique = df_all.drop_duplicates(subset=df1.columns.difference(['source']), keep=False)

# Separate the unique rows from each file
df_unique_file1 = df_unique[df_unique['source'] == 'file1'].drop(columns=['source'])
df_unique_file2 = df_unique[df_unique['source'] == 'file2'].drop(columns=['source'])

# Save the differences to new CSV files
df_unique_file1.to_csv("differences_file1.csv", index=False)
df_unique_file2.to_csv("differences_file2.csv", index=False)

print("Differences saved to 'differences_file1.csv' and 'differences_file2.csv'")
