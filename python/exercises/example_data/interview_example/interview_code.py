from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])
m = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawmapboundary()
m.drawcoastlines()

dataset = Dataset("tas_rcp45_2055_mon_avg_change.nc")
timevar = dataset.variables['time']
tas = dataset.variables['tas'][0,:].squeeze()
lats = dataset.variables['lat'][:]
lons = dataset.variables['lon'][:]

lons_mesh, lats_mesh = np.meshgrid(lons, lats)

mesh = m.pcolormesh(lons_mesh, lats_mesh, tas, shading='flat', cmap=plt.cm.jet, latlon=True)
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))
cb = m.colorbar(mesh, "bottom", size="5%", pad="2%")
ax.set_title('Change in Surface Air Temperature (RCP45, monthly average)')
plt.savefig("tas_plot.png")
plt.show()
