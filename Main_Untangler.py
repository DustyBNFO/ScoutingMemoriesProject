#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:48:21 2024

@author: dustyzeliff
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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
        self.merge_to = [mt.strip() for mt in merge_to.split(',')] if isinstance(merge_to, str) else []
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
nodes_dict = {}  # Dictionary to store nodes by council_id for quick lookup

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
    nodes_dict[row['council_id']] = node

# Step 4: Create the plot area
fig, ax = plt.subplots(figsize=(200, 5))  # Adjust the width for more space between ticks

# Set the X-axis limits from 1900 to 2025
ax.set_xlim(1900, 2025)

# Set the Y-axis limits to a fixed range (0 to 100 for now)
ax.set_ylim(0, 100)

# Add X-axis ticks and labels for every year from 1900 to 2025
ax.set_xticks(np.arange(1900, 2026, 1))
ax.set_xticklabels(np.arange(1900, 2026, 1), rotation=90)

# Add X-axis label
ax.set_xlabel('Year')
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top()
ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5)

# Remove Y-axis label
ax.get_yaxis().set_visible(False)

# Step 5: Draw boxes and arrows for each node
box_height = 10
min_width = 1  # Minimum width corresponding to one tick
box_positions = {}  # Store the positions of each box

for i, node in enumerate(nodes):
    start = node.start
    end = node.end
    width = max(end - start, min_width)  # Ensure minimum width is met
    y_position = i * (box_height + 5)  # Adjust vertical position with some spacing
    box_positions[node.council_id] = (start, width, y_position)
    
    rect = patches.Rectangle((start, y_position), width, box_height, linewidth=1, edgecolor='black', facecolor='lightblue')
    ax.add_patch(rect)
    ax.text(start + width / 2, y_position + box_height / 2, node.name + " Council" +"\n" + node.city_county + "," +node.state + " " + str(node.start) + " - " + str(node.end), ha='center', va='center', fontsize=10)
    
    # Draw arrows from the merge date points
    for merge_date, merge_to_id in zip(node.merge_date, node.merge_to):
        merge_date = int(merge_date)
        if merge_to_id in nodes_dict and merge_to_id in box_positions:
            merge_to_node = nodes_dict[merge_to_id]
            merge_to_start, merge_to_width, merge_to_y_position = box_positions[merge_to_node.council_id]
            arrow = patches.FancyArrowPatch(
                (merge_date, y_position + box_height),
                (merge_to_start, merge_to_y_position),
                arrowstyle='->', mutation_scale=10, color='black'
            )
            ax.add_patch(arrow)

# Display the plot
plt.title("Node Boxes and Arrows on Plot")
plt.gca().invert_yaxis()  # Invert the Y-axis
plt.show()

