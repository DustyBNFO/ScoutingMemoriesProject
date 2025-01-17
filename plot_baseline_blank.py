#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:18:44 2024

@author: dustyzeliff
"""

import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis with a larger width
fig, ax = plt.subplots(figsize=(20, 5))  # Adjust the width (15) for more space between ticks

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

# Display the plot
plt.title("Inverted Plot Area with Expanded Tick Space")
plt.gca().invert_yaxis()  # Invert the Y-axis

plt.show()
