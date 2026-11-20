# KalingaKavach

### AI-Powered Early Warning and Monitoring for Odisha's Mangroves

> *Kalinga's shield: turning satellite data into timely action for the coast.*

---

## Abstract

Odisha's mangroves, from Bhitarkanika to the Mahanadi delta, are the state's natural shield against cyclones such as Phailin, Fani, and Yaas. They also store carbon, protect shorelines from erosion, and sustain the fishing communities along the coast. Yet they are under pressure from aquaculture expansion, land conversion, pollution, and climate change. Most monitoring today is reactive: damage is found through slow, costly field surveys, often after it can no longer be reversed.

KalingaKavach is an AI-powered system that turns satellite imagery into early warning and decision support. It compares Sentinel-2 imagery across time, including pre- and post-cyclone periods, to find canopy loss, and gives each flagged location a priority score based on its size so forest staff know where to act first. A web dashboard lets supervisors review alerts, assign field teams, and record verification on the ground.

---

## Problem Statement

- Odisha has a long, cyclone-prone coastline where mangroves are a critical natural defence.
- Mangroves are declining due to aquaculture, land conversion, pollution, sea-level rise, and storms.
- Field surveys are slow, costly, and hard to repeat in muddy, creek-dense, hard-to-reach areas.
- Authorities often learn about damage late, when restoration is harder.

## Our Solution

KalingaKavach shifts mangrove protection from **reaction to prevention** by automatically detecting and prioritising changes in mangrove cover using satellite imagery, then connecting each alert to a field team that can verify it.

---

## Key Features

| Feature | Status |
|---|---|
| **Change detection:** compares two dates and finds canopy loss, with a cloud mask and area in hectares | Built, tested on synthetic data |
| **Priority scoring:** ranks flagged areas P1 to P3 by size, with a confidence score | Built |
| **Post-cyclone damage mapping:** the same pipeline run on pre- and post-cyclone imagery (Cyclone Dana, October 2024 is the first test case) | Script ready, not yet run on real imagery |
| **Web dashboard:** overview, alert queue, map, field teams, reports, activity log | Built |
| **Field verification workflow:** assign a team, mark verified, reopen, report an incident from the field | Built |
| **Shared database:** alerts, teams and activity are saved and shared between users | Built |
| **Alert API:** FastAPI service with an API key and a hook for SMS or WhatsApp on P1 alerts | Written, not yet deployed |
| **Mangrove classification (dense, sparse, open)** | Planned |
| **Cause separation (regrowth, storm damage, human-driven loss)** | Planned, needs ranger-labelled examples |
| **Restoration tracking and carbon estimation** | Planned |

---

## How It Works

```
Sentinel-2 imagery  ->  Cloud mask + NDVI  ->  Change detection  ->  Priority scoring
                                                                           |
                        Dashboard and alerts  <-  Alert API  <-------------+
                                  |
                       Field team verifies  ->  Result saved back to the record
```

1. **Data collection:** Before and after Sentinel-2 composites of the Odisha coast, exported from Google Earth Engine
2. **Preprocessing:** Cloud and shadow masking from the scene classification band, then NDVI
3. **Change detection:** Pixels that were healthy canopy and lost a set amount of NDVI are grouped into regions
4. **Prioritisation:** Each region gets an area in hectares, a P1 to P3 priority, and a score
5. **Output:** Alerts go to the API and dashboard, where staff assign teams and record verification

---

## Tech Stack

- **Satellite data:** Sentinel-2 (ESA Copernicus), accessed through Google Earth Engine
- **Language:** Python 3, JavaScript
- **Geospatial tools:** NumPy, SciPy, rasterio
- **Models:** NDVI thresholding with connected-region analysis (a learned classifier is planned)
- **Backend:** FastAPI, SQLite
- **Dashboard:** Single-page web app in plain HTML, CSS and JavaScript (Instrument Sans and IBM Plex Mono)

---

## Study Area

- **Primary region:** Bhitarkanika, Kendrapara
- **Other sites:** Mahanadi delta, Chilika fringe
- **Time period:** 2018 to 2025 planned; the first backtest uses Cyclone Dana (October 2024)

---

## Project Structure

```
KalingaKavach/
|-- backend/
|   |-- app.py             # FastAPI service: alerts, teams, activity
|   |-- detect.py          # Cloud mask, NDVI, change detection, priority
|   `-- run_detect.py      # Reads two GeoTIFFs and posts alerts to the API
|-- gee/
|   `-- export_sentinel2.js  # Earth Engine export of pre and post composites
|-- dashboard/
|   `-- index.html         # Web dashboard
|-- tests/
|   `-- test_detect.py     # Detection tests on synthetic scenes
|-- requirements.txt
`-- README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# 1. Run the detection tests
python tests/test_detect.py

# 2. Export imagery: paste gee/export_sentinel2.js into code.earthengine.google.com,
#    run both exports, and download kk_pre.tif and kk_post.tif from Google Drive

# 3. Try detection on real imagery without posting anything
cd backend
python run_detect.py kk_pre.tif kk_post.tif --dry

# 4. Start the API (set KK_API_KEY first to protect write endpoints)
uvicorn app:app --reload        # docs at http://localhost:8000/docs

# 5. Post the detected alerts to the API
python run_detect.py kk_pre.tif kk_post.tif --api http://localhost:8000 --key YOUR_KEY
```

Open `dashboard/index.html` in a browser to use the dashboard.

---

## Results

Real-imagery results have not been measured yet. This section will be filled in after the Cyclone Dana backtest.

- **Detection on synthetic scenes:** 3 of 3 tests pass (finds a known 9 ha loss, ignores cloud-masked pixels, ignores small noise)
- **Change detection performance on real imagery:** `[precision / recall / F1 against hand-drawn polygons, to be measured]`
- **Classification accuracy:** `[to be measured once the classifier is added]`
- **Sample outputs:** `[add before and after imagery, the detected regions, and dashboard screenshots]`

---

## Limitations

- The NDVI drop and minimum-canopy thresholds are starting values and need tuning on real scenes.
- Tidal flooding and monsoon cloud also change NDVI. Sentinel-1 radar and a tide filter are planned.
- Alerts are labelled "Unclassified canopy loss". Cause is not inferred until there are labelled examples from field verification.
- The dashboard currently runs on its own shared database. Connecting it to the FastAPI service is the next integration step.
- The dashboard map is a stylised sketch. A real map with polygons and a satellite basemap is planned.

---

## Impact

- **Environmental:** Earlier detection of mangrove loss and faster restoration response
- **Climate resilience:** Stronger protection against cyclones and coastal erosion
- **Climate action:** Supports blue-carbon assessment and planning once carbon estimation is added
- **Community:** Protects the fisheries and livelihoods that depend on mangroves
- **Scalability:** Low-cost approach that can extend to other coastal states

---

## Future Scope

- Mangrove classification into dense, sparse and open cover
- Cause separation trained on ranger-verified alerts
- Sentinel-1 radar for cloudy months
- Real map with polygons and satellite basemap
- Offline-capable mobile view for field staff
- Near-real-time satellite feeds and SMS alerts
- Expansion to other coastal states of India
- Collaboration with forest departments and research institutions

---

## Team

| Name | Role |
|---|---|
| Aryan Shankar Pradhan | Project Lead |
| Anwesha Nayak | Tech Lead |
| Hanshraj Sethi | Data and Design |
| Amaan Ali Khan | Research and Documentation |

---

## Acknowledgements

- ESA Copernicus for Sentinel-2 data and Google Earth Engine for processing access
- Siksha 'O' Anusandhan

---

<p align="center"><b>KalingaKavach: protecting Odisha's coast, one mangrove at a time.</b></p>
