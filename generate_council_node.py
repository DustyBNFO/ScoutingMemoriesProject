#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:33:51 2024

@author: dustyzeliff
"""

import pandas as pd

# Step 1: Read the CSV file
csv_file = 'HOVTest.csv'
df = pd.read_csv(csv_file)

# Step 2: Define the Node class
class Node:
    def __init__(self, council_id, name, city_county, state, start, end, merge_date, merge_to, name_change, is_current, council_no, history, link, description):
        self.council_id = council_id
        self.name = name
        self.city_county = city_county
        self.state = state
        self.start = start
        self.end = end
        self.merge_date = [date.strip() for date in merge_date.split(',')] if isinstance(merge_date, str) else [merge_date]
        self.merge_to = [mt.strip() for mt in merge_to.split(',')] if isinstance(merge_to, str) else [merge_to]
        self.name_change = name_change
        self.is_current = is_current
        self.council_no = council_no
        self.history = history
        self.link = link
        self.description = description
    
    def __str__(self):
        return (f"ID: {self.council_id}, Name: {self.name}, Location: {self.city_county}, State: {self.state}, Start: {self.start}, End: {self.end}, "
                f"Merge Date: {self.merge_date}, Merge To: {self.merge_to}, Name Change: {self.name_change}, Is Current: {self.is_current}, "
                f"Council Number: {self.council_no}, History: {self.history}, Link: {self.link}, Description: {self.description}")

# Step 3: Create nodes based on the CSV data
nodes = []

for index, row in df.iterrows():
    merge_date = row['merge date']
    merge_to = row['merge to']

    node = Node(
        council_id=row['council_id'],
        name=row['name'],
        city_county=row['city_county'],
        state=row['state'],
        start=row['start'],
        end=row['end'],
        merge_date=merge_date,
        merge_to=merge_to,
        name_change=row['name change to'],
        is_current=row['is_current'],
        council_no=row['council_no'],
        history=row['history'],
        link=row['link'],
        description=row['description']
    )
    nodes.append(node)

# Display all aspects of the nodes
# for node in nodes:
#     print(node)
#     print("-----")

