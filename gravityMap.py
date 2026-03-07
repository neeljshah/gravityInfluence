import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
from scipy.spatial import ConvexHull
import pandas as pd
import numpy as np

# 1. CLEAN DATA
df = dataset.dropna(subset=['LOC_X', 'LOC_Y'])

# 2. COURT DRAWING FUNCTION
def draw_court(ax=None, color='white', lw=1):
    if ax is None: ax = plt.gca()
    # Hoop & Backboard
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)
    # Paint & Restricted Area
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw, color=color, fill=False)
    # 3pt Line Arc
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color, fill=False)
    corner_three_left = Rectangle((-220, -47.5), 0, 140, linewidth=lw, color=color)
    corner_three_right = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
    
    court_elements = [hoop, backboard, outer_box, restricted, three_arc]
    for element in court_elements: ax.add_patch(element)
    ax.plot([-220, -220], [-47.5, 92.5], linewidth=lw, color=color)
    ax.plot([220, 220], [-47.5, 92.5], linewidth=lw, color=color)
    return ax

# 3. SETUP PLOT
fig = plt.figure(figsize=(5, 4.7))
ax = fig.add_axes([0, 0, 1, 1])
fig.patch.set_facecolor('#141414')
ax.set_facecolor('#141414')

# Draw Court
draw_court(ax, color='#333333', lw=1.5)

# 4. CALCULATE CONVEX HULL (The Gravity Area)
points = df[['LOC_X', 'LOC_Y']].values
if len(points) > 5:
    try:
        hull = ConvexHull(points)
        # Draw the Shaded Gravity Zone
        plt.fill(points[hull.vertices,0], points[hull.vertices,1], 
                 color='#FFD700', alpha=0.15, label='Gravity Perimeter')
        # Draw the Gold Perimeter Line
        for simplex in hull.simplices:
            plt.plot(points[simplex, 0], points[simplex, 1], color='#FFD700', lw=2, alpha=0.8)
        
        # Display Area Score
        area_score = int(hull.area / 100)
        plt.text(-230, 420, f"GRAVITY SCORE: {area_score}", color='#FFD700', 
                 fontsize=14, fontweight='bold', family='sans-serif')
    except:
        pass

# 5. PLOT SHOTS
made = df[df['SHOT_MADE_FLAG'] == 1]
missed = df[df['SHOT_MADE_FLAG'] == 0]

plt.scatter(missed.LOC_X, missed.LOC_Y, color='#FF4B4B', alpha=0.3, s=15)
plt.scatter(made.LOC_X, made.LOC_Y, color='#00FFCC', alpha=0.6, s=15)

# Limits & Formatting
plt.xlim(-250, 250)
plt.ylim(-50, 450)
plt.axis('off')

plt.show()
