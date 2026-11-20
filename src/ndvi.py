import rasterio
import numpy as np
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

def calculate_ndvi(tile_name):
    tile_dir = RAW_DIR / tile_name

    # Find Red and Near Infrared bands
    red_files = list(tile_dir.glob("*B04*.jp2"))
    nir_files = list(tile_dir.glob("*B08*.jp2"))

    if not red_files or not nir_files:
        raise FileNotFoundError(f"B04 or B08 missing in {tile_name}")

    with rasterio.open(red_files[0]) as red_src, \
         rasterio.open(nir_files[0]) as nir_src:

        if (red_src.shape != nir_src.shape or
            red_src.transform != nir_src.transform or
            red_src.crs != nir_src.crs):
            raise ValueError(f"Band alignment mismatch in {tile_name}")

        red = red_src.read(1).astype("float32")
        nir = nir_src.read(1).astype("float32")

        denominator = nir + red

        valid = (
            (red_src.read_masks(1) > 0) &
            (nir_src.read_masks(1) > 0) &
            np.isfinite(red) &
            np.isfinite(nir) &
            (denominator != 0)
        )

        ndvi = np.full(red.shape, -9999, dtype="float32")

        ndvi[valid] = (
            (nir[valid] - red[valid]) /
            denominator[valid]
        )

        profile = red_src.profile.copy()
        profile.update(
            driver="GTiff",
            dtype="float32",
            count=1,
            nodata=-9999,
            compress="deflate"
        )

    output_file = OUTPUT_DIR / f"NDVI_{tile_name}.tif"

    with rasterio.open(output_file, "w", **profile) as dst:
        dst.write(ndvi, 1)

    print(f"NDVI saved: {output_file}")

    if valid.any():
        print("Mean NDVI:", float(ndvi[valid].mean()))


if __name__ == "__main__":
    calculate_ndvi("45QVD")
    calculate_ndvi("45QVC")