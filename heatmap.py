# Prolog - Auto Generated #
import os, uuid, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import pandas

import sys
sys.tracebacklimit = 0

os.chdir(u'C:/Users/neelj/PythonEditorWrapper_23a47bad-efdb-4f00-8cf8-ee21fc1dbbf4')
dataset = pandas.read_csv('input_df_2b212104-3eae-4a3a-bd31-7c891a731b23.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667), dpi=72)
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
from scipy.spatial import ConvexHull
import pandas as pd
import numpy as np

# 1. Clean data
df = dataset.dropna(subset=['LOC_X', 'LOC_Y'])

def draw_court(ax=None, color='white', lw=1):
    if ax is None: ax = plt.gca()
    # Hoop, Paint, and Restricted Area
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw, color=color, fill=False)
    # 3pt Arc and Corners
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color, fill=False)
    ax.plot([-220, -220], [-47.5, 92.5], linewidth=lw, color=color)
    ax.plot([220, 220], [-47.5, 92.5], linewidth=lw, color=color)
    
    court_elements = [hoop, outer_box, restricted, three_arc]
    for element in court_elements: ax.add_patch(element)
    return ax

# Setup Plot
fig = plt.figure(figsize=(5, 4.7))
ax = fig.add_axes([0, 0, 1, 1])
fig.patch.set_facecolor('#141414')
ax.set_facecolor('#141414')

# --- LAYER 1: THE HEATMAP (Density) ---
# We use hexbin to show concentration of threat
if len(df) > 10:
    hb = ax.hexbin(df.LOC_X, df.LOC_Y, gridsize=25, cmap='YlOrRd', mincnt=1, alpha=0.5, edgecolors='none')


# --- LAYER 3: THE COURT LINES ---
# We draw lines on top so they are visible over the heatmap
draw_court(ax, color='#FFFFFF', lw=1.2)

# Formatting
plt.xlim(-250, 250)
plt.ylim(-50, 450)
plt.axis('off')

plt.show()

# Epilog - Auto Generated #
os.chdir(u'C:/Users/neelj/PythonEditorWrapper_23a47bad-efdb-4f00-8cf8-ee21fc1dbbf4')
