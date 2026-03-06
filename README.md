# 🌌 Defensive Gravity Model
### Part 3 of the Basketball Intelligence Suite

> **Measuring the invisible force — quantifying how much defensive attention a player commands without touching the ball.**

---

## 📸 Dashboard Preview

![Defensive Gravity Dashboard](demo.gif)

> *Interactive Power BI dashboard — filter by Player, Team, and Matchup to explore gravity and elasticity across the league.*

---

## 🔍 What This Project Does

The best scorers in basketball don't just score — they *warp the defense around them*, creating open looks for teammates by simply being on the floor. This is **gravity**: a player's ability to pull defenders away from their assignments.

The **Defensive Gravity Model** quantifies this off-ball influence using Euclidean spatial analysis. It also introduces **Elasticity** — measuring how much a player's efficiency fluctuates based on defensive pressure — to reveal who stays consistent under duress and who wilts.

---

## 📊 Dashboard Breakdown

### Elasticity Scatter Plot
- **X-axis:** Average Gravity — the spatial force a player exerts on opposing defenders (measured in Euclidean defender displacement units)
- **Y-axis:** Average Elasticity — how much a player's performance varies under different levels of defensive pressure
- **Bubble size:** Shot volume
- High Gravity + Low Elasticity = **elite, pressure-resistant scorer**
- High Gravity + High Elasticity = **streaky, pressure-dependent scorer**

### Heat Map
- Spatial density map of a player's shot origins overlaid on the half-court
- Bright red core = highest shot concentration zones
- Reveals where defenders *must* respect a player's threat

### Average Shot Zone
- A simplified court zone visual showing the player's primary area of operation
- Green fill = dominant zone, cross marker = centroid of shot activity

### Gravity Score Card
- A single numerical gravity score (displayed in yellow) representing the total defensive displacement a player generates
- Higher score = more defenders pulled further from their assignments

### Shot Map
- Full court scatter of every shot attempt with directional lines from origin point
- Yellow dots/lines show shot trajectory patterns — reveals pull-up range, drive angles, and post-up tendencies

---

## ⚙️ Tech Stack

| Tool | Usage |
|---|---|
| **Power BI** | Dashboard, spatial visualizations, DAX gravity scoring |
| **Python (NumPy, SciPy)** | Euclidean distance calculations, KDE spatial modeling |
| **NBA Stats API / Tracking Data** | Defender positioning, shot coordinate data |
| **DAX** | Gravity Score aggregation, elasticity variance calculations |

---

## 🧠 Key Insight

> **LeBron James** and **Kevin Durant** both post high Gravity Scores (10K+ range) but differ significantly in Elasticity — LeBron maintains near-zero elasticity variance under pressure, while high-volume perimeter shooters show much wider elasticity swings. This confirms that gravity without consistency is a defensive luxury, not a nightmare.

---

## 🧮 Gravity Score Formula

```
Gravity Score = Σ (Defender_Displacement × Shot_Threat_Weight × Court_Zone_Multiplier)

Where:
  Defender_Displacement = Euclidean distance defender moves from their assignment
  Shot_Threat_Weight    = based on historical FG% from that zone
  Court_Zone_Multiplier = 3PT zones weighted higher than mid-range
```

---

## 🚀 How to Use

1. Clone the repo and open the `.pbix` file in Power BI Desktop
2. Use **Player Name**, **Team Name**, and **Matchup** filters to explore any player
3. The Elasticity chart plots all players league-wide — use it to find outliers
4. Select a specific player to isolate their Heat Map, Shot Zone, and Gravity Score

---

## 📁 Repository Structure

```
Defensive-Gravity/
├── data/
│   └── tracking_data_cleaned.csv
├── notebooks/
│   └── gravity_model.ipynb
├── dashboard/
│   └── DefensiveGravity.pbix
└── README.md
```

---

## 🔗 Part of the Basketball Intelligence Suite

| Part | Project | Focus |
|---|---|---|
| **1** | Spatial Efficiency Engine | Shot quality & creation mapping |
| **2** | Momentum Volatility Index | Game-flow & run detection |
| **3** | Defensive Gravity Model *(you are here)* | Off-ball spatial influence |
| **4** | Behavioral Archetyping | Player segmentation & style |
