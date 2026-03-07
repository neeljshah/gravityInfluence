import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
import pandas as pd

# 1. Clean data
df = dataset.dropna(subset=['LOC_X', 'LOC_Y'])

# 2. Setup Plot
fig, ax = plt.subplots(figsize=(5, 4.7))
fig.patch.set_facecolor('#141414')
ax.set_facecolor('#141414')

# 3. CALCULATE THE CONFIDENCE ELLIPSE (The Math Layer)
if len(df) > 5:
    x = df['LOC_X']
    y = df['LOC_Y']
    
    # Calculate Mean and Covariance
    mu = np.mean(x), np.mean(y)
    cov = np.cov(x, y)
    
    # Calculate Eigenvalues for orientation
    vals, vecs = np.linalg.eigh(cov)
    order = vals.argsort()[::-1]
    vals, vecs = vals[order], vecs[:,order]
    theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))
    
    # Draw the Ellipse (Width/Height based on 2 Standard Deviations)
    w, h = 2 * 2 * np.sqrt(vals)
    ell = Ellipse(xy=mu, width=w, height=h, angle=theta, 
                  edgecolor='#00FFCC', fc='#00FFCC', lw=2, alpha=0.2)
    ax.add_patch(ell)
    
    # Add a "Center of Gravity" marker
    plt.scatter(mu[0], mu[1], color='#00FFCC', s=100, marker='+', linewidths=3)

# 4. COURT OVERLAY
plt.plot([-250, 250], [0, 0], color='white', lw=1, alpha=0.3) # Baseline
plt.xlim(-250, 250)
plt.ylim(-50, 450)
plt.axis('off')
plt.show()
