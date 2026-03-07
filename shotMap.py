import matplotlib.pyplot as plt
import pandas as pd

# 1. Clean data
df = dataset.dropna(subset=['LOC_X', 'LOC_Y'])

# 2. Setup Plot
fig = plt.figure(figsize=(5, 4.7))
ax = fig.add_axes([0, 0, 1, 1])
fig.patch.set_facecolor('#141414')
ax.set_facecolor('#141414')

# 3. DRAW VECTORS (The "Tech" Layer)
# We draw a line from the shot to the hoop (0,0)
for i, row in df.iterrows():
    plt.plot([row['LOC_X'], 0], [row['LOC_Y'], 0], 
             color='#FFD700', alpha=0.1, lw=0.5)

# 4. PLOT SHOT ORIGINS
plt.scatter(df.LOC_X, df.LOC_Y, color='#FFD700', s=10, alpha=0.6)

# 5. HIGHLIGHT THE HOOP (The Target)
hoop = plt.Circle((0, 0), 10, color='white', fill=True, alpha=0.8)
ax.add_patch(hoop)

plt.xlim(-250, 250)
plt.ylim(-50, 450)
plt.axis('off')
plt.show()
