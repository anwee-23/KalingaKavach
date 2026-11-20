# KalingaKavach – NDVI Methodology

## 1. Satellite Data
Source: Sentinel-2 Level-2A
Study Area: Bhitarkanika, Odisha

Required bands:
- B04: Red (10m)
- B08: Near Infrared (10m)
- SCL: Scene Classification Layer (20m)

## 2. NDVI Calculation

Formula:

NDVI = (B08 - B04) / (B08 + B04)

NDVI ranges from -1 to +1.

Higher positive values generally indicate stronger vegetation signals.

## 3. Cloud Masking

Use the Sentinel-2 SCL layer to exclude:
- No-data pixels
- Saturated or defective pixels
- Cloud shadows
- Cloud and cirrus pixels

Resample the classification mask to match the 10m NDVI grid using nearest-neighbour resampling.

## 4. Vegetation Decline Measurement

Use two cloud-free Sentinel-2 observations from different dates.

Calculate:

NDVI Change = Later NDVI - Earlier NDVI

Negative values indicate a decrease in NDVI.

Calculate vegetation decline percentage as:

Decline (%) =
(Number of valid mangrove pixels with NDVI change <= -0.10
 / Total valid mangrove pixels) * 100

The -0.10 threshold is an initial working threshold and must be validated.

## 5. Important Conditions

- Compare the same geographical area.
- Use comparable seasonal observations.
- Apply cloud and shadow masking.
- Restrict calculations to the mangrove study boundary.
- Do not interpret NDVI decline alone as proof of mangrove loss.
