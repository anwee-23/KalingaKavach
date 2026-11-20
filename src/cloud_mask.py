import rasterio
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
OUTPUT_DIR = BASE_DIR / "outputs"

# SCL classes to exclude:
# 0 = No data
# 1 = Saturated/defective pixels
# 3 = Cloud shadows
# 7 = Low probability clouds / unclassified
# 8 = Medium probability clouds
# 9 = High probability clouds
# 10 = Cirrus
# 11 = Snow/ice

BAD_CLASSES = [0, 1, 3, 7, 8, 9, 10, 11]

for tile in ["45QVD", "45QVC"]:

    folder = RAW_DIR / tile
    scl_file = next(folder.glob("*SCL*.jp2"))

    with rasterio.open(scl_file) as src:
        scl = src.read(1)
        profile = src.profile.copy()

    cloud_mask = np.isin(scl, BAD_CLASSES)

    profile.update(
        driver="GTiff",
        dtype="uint8",
        count=1,
        nodata=255
    )

    output_file = OUTPUT_DIR / f"CloudMask_{tile}.tif"

    with rasterio.open(output_file, "w", **profile) as dst:
        dst.write(cloud_mask.astype("uint8"), 1)

    print(f"Cloud mask saved: {output_file}")
    print(f"Masked pixels: {np.sum(cloud_mask)}")