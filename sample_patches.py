import sys
from osgeo import gdal
import numpy as np

# Extract tiles from remote sensing image, into numpy array

TILESIZE=256

filename = sys.argv[1]

S = gdal.Open(filename)


for x in range(0, S.RasterXSize, TILESIZE)[:-1]:
    patches = []
    print x
    for y in range(0, S.RasterYSize, TILESIZE)[:-1]:
        A = np.transpose(S.ReadAsArray(x,y,TILESIZE,TILESIZE))
        if not np.isnan(A).any() and np.min(A) > 0:
            patches.append(A)
	
    patches = np.array(patches)
    np.save('images_set'+str(x)+'.npy', patches)
