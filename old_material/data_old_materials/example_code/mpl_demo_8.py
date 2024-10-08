from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset, date2index
import numpy as np
import matplotlib.pyplot as plt
# Open a remote netCDF dataset.
dataset = Dataset("../example_data/tas_rcp45_2055_mon_avg_change.nc")
timevar = dataset.variables['time']
tas = dataset.variables['tas'][0,:].squeeze()
lats = dataset.variables['lat'][:]
lons = dataset.variables['lon'][:]
lons, lats = np.meshgrid(lons,lats)
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])
#m = Basemap(projection='kav7',lon_0=0,resolution=None)
m = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')
m.drawmapboundary(fill_color='0.3')
m.drawcoastlines()
im1 = m.pcolormesh(lons,lats,tas,shading='flat',cmap=plt.cm.jet,latlon=True)
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))
cb = m.colorbar(im1,"bottom", size="5%", pad="2%")
ax.set_title('Change in Surface Air Temperature from MOHC HadGEM2-ES')
plt.show()
