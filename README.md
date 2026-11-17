# KalingaKavach

### AI-Powered Early Warning and Monitoring for Odisha's Mangroves

> *Kalinga's shield: turning satellite data into timely action for the coast.*

---

## Abstract

Odisha's mangroves, from Bhitarkanika to the Mahanadi delta, are the state's natural shield against cyclones such as Phailin, Fani, and Yaas. They also store carbon, protect shorelines from erosion, and sustain the fishing communities along the coast. Yet they are under pressure from aquaculture expansion, land conversion, pollution, and climate change. Most monitoring today is reactive: damage is found through slow, costly field surveys, often after it can no longer be reversed.

KalingaKavach is an AI-powered system that turns satellite imagery into early warning and decision support. It uses machine learning and deep learning models to classify mangrove cover into dense, sparse, and open categories. It then compares imagery across time and across pre- and post-cyclone periods to separate natural regrowth, storm damage, and human-driven loss such as illegal clearing or encroachment. Each flagged location receives a priority score based on the size, speed, and type of change, so forest staff know where to act first.

---

## Problem Statement

- Odisha has a long, cyclone-prone coastline where mangroves are a critical natural defence.
- Mangroves are declining due to aquaculture, land conversion, pollution, sea-level rise, and storms.
- Field surveys are slow, costly, and hard to repeat in muddy, creek-dense, hard-to-reach areas.
- Authorities often learn about damage late, when restoration is harder.

## Our Solution

KalingaKavach shifts mangrove protection from **reaction to prevention** by automatically detecting, classifying, and prioritising changes in mangrove cover using satellite imagery.

---

## Key Features

| Feature | Description |
|---|---|
| **Mangrove classification** | Classifies cover into dense, sparse, and open categories |
| **Change detection** | Compares imagery over time to find loss, degradation, and regrowth |
| **Post-cyclone damage maps** | Compares pre- and post-cyclone imagery to map storm damage quickly |
| **Priority scoring** | Ranks flagged locations by size, speed, and type of change |
| **Automated alerts** | Notifies authorities when rapid degradation is detected |
| **Restoration tracking** | Shows whether replanted areas are actually recovering |
| **Carbon estimation** | Estimates carbon stock changes for blue-carbon planning |
| **Web dashboard** | Simple interface that non-technical users can read |

> **Note:** Update this table to list only the features implemented in your current version.

---

## How It Works

```
Satellite Imagery  →  Preprocessing  →  AI Classification  →  Change Detection
                                                                      ↓
        Dashboard & Alerts  ←  Priority Scoring  ←  Change Type Analysis
```

1. **Data collection:** Multi-temporal satellite images of the Odisha coast
2. **Preprocessing:** Cloud masking, correction, and index calculation (e.g. NDVI)
3. **Classification:** Model labels pixels as dense, sparse, or open mangrove
4. **Change detection:** Compares time periods to find loss, degradation, or regrowth
5. **Cause separation:** Distinguishes natural regrowth, storm damage, and human-driven loss
6. **Prioritisation:** Scores each flagged area so action goes where it is needed first
7. **Output:** Maps, alerts, and dashboard views for decision makers

---

## Tech Stack

> Replace the placeholders below with what you actually use.

- **Satellite data:** ` `
- **Language:** ` `
- **Geospatial tools:** ` `
- **Models:** ` `
- **ML frameworks:** ` `
- **Dashboard:** ` `

---

## Study Area

- **Primary region:** `Bhitarkanika, Kendrapara`
- **Other sites:** `Mahanadi delta, Chilika fringe`
- **Time period analysed:** `2018 to 2025`

---

## Project Structure

```
KalingaKavach/

└── README.md
```

> Adjust this to match your real folder layout.

---

## Installation

```bash

```

## Usage

```bash

```

> Update the commands to match your project.

---

## Results

> Add your real results here. Judges look for evidence.

- **Classification accuracy:** `[e.g. 9X%]`
- **Change detection performance:** `[precision / recall / F1]`
- **Sample outputs:** add images of classified maps, change maps, and the dashboard

```
![Mangrove classification map](outputs/classification_map.png)
![Change detection map](outputs/change_map.png)
![Dashboard screenshot](outputs/dashboard.png)
```

---

## Impact

- **Environmental:** Earlier detection of mangrove loss and faster restoration response
- **Climate resilience:** Stronger protection against cyclones and coastal erosion
- **Climate action:** Supports blue-carbon assessment and planning
- **Community:** Protects the fisheries and livelihoods that depend on mangroves
- **Scalability:** Low-cost approach that can extend to other coastal states

---

## Future Scope

- Integration with real-time or near-real-time satellite feeds
- Mobile app for field staff to verify alerts on the ground
- Species-level mangrove mapping
- Expansion to other coastal states of India
- Collaboration with forest departments and research institutions

---

## Team

| Name | Role |
|---|---|
| `[Your Name]` | `[Role]` |
| `[Teammate]` | `[Role]` |

---

## Acknowledgements

- Satellite data providers `[e.g. ESA Copernicus, USGS]`
- `[Competition or organisation name]`
- `[Mentors, institutions, or open-source tools]`

---

## License

This project is licensed under the `[MIT]` License. See the `LICENSE` file for details.

---

<p align="center"><b>KalingaKavach: protecting Odisha's coast, one mangrove at a time.</b></p>
