import sys
from osgeo import gdal
import numpy as np

# Extract tiles from remote sensing image, into numpy array

TILESIZE=256

filename = sys.argv[1]

S = gdal.Open(S)
A = np.transpose(S.ReadAsArray(), (1,2,0))

patches = []

for x in range(0, S.RasterXSize, TILESIZE):
    for y in range(0, S.RasterYSize, TILESIZE):
        A = np.transpose(S.ReadAsArray(x,y,TILESIZE,TILESIZE))
        if not np.isnan(A).any():
            patches.append(A)

patches = np.array(patches)
np.save('images_set.npy', patches)
