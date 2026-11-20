import rasterio
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"

for tile in ["45QVD", "45QVC"]:

    file_path = OUTPUT_DIR / f"NDVI_{tile}.tif"

    with rasterio.open(file_path) as src:
        ndvi = src.read(1)
        nodata = src.nodata

    if nodata is not None:
        ndvi = np.ma.masked_equal(ndvi, nodata)

    plt.figure(figsize=(10, 8))

    plt.imshow(
        ndvi,
        cmap="RdYlGn",
        vmin=-1,
        vmax=1
    )

    plt.colorbar(label="NDVI")
    plt.title(f"KalingaKavach - NDVI {tile}")
    plt.axis("off")

    output_file = OUTPUT_DIR / f"NDVI_{tile}.png"

    plt.savefig(
        output_file,
        bbox_inches="tight",
        dpi=200
    )

    plt.close()

    print(f"Map saved: {output_file}")