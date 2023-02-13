# Import Basemap to manage map projections, plotting of boundaries etc
from mpl_toolkits.basemap import Basemap
# Import netCDF4 to read data from NetCDF file
from netCDF4 import Dataset
# Import numpy to provide the .meshgrid and .arange functions
import numpy as np
# Import the Pyplot interface from Matplotlib to set up the figure and plot the data
import matplotlib.pyplot as plt

# Create the figure and configure the borders
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])

# Generate a Basemap projection to display the globe on, defining the domain and resolution.
m = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
# Draw the map boundary and the coastlines
m.drawmapboundary()
m.drawcoastlines()

# Use the NetCDF4 Dataset class to open a NetCDF file
dataset = Dataset("tas_rcp45_2055_mon_avg_change.nc")

# Extract arrays for time, lats and lons
timevar = dataset.variables['time']
lats = dataset.variables['lat'][:]
lons = dataset.variables['lon'][:]

# Extract 2D surface temperature array (squeeze out singleton dimensions)
tas = dataset.variables['tas'][0,:].squeeze()

# Create meshgrid values for each point (so lats and lons are known at every cell on grid)
lons_mesh, lats_mesh = np.meshgrid(lons, lats)

# Create colormesh to plot each grid cell with the correct colour,
# using colormap called "plt.cm.jet"
mesh = m.pcolormesh(lons_mesh, lats_mesh, tas, shading='flat', cmap=plt.cm.jet, latlon=True)

# Draw horizontal and vertical gridlines over map at regular intervals
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))

# Define the colorbar at the bottom of the image
cb = m.colorbar(mesh, "bottom", size="5%", pad="2%")

# Set the title
ax.set_title('Change in Surface Air Temperature (RCP45, monthly average)')

# Save the figure to a PNG file 
plt.savefig("tas_plot.png")

# Display the figure
plt.show()

# Any comments on this code. I hope they might say:
"""
 1. No commments - bad
 2. No functions/classes - bad
 3. They might suggest more elegant solutions
 4. They might comment on pyplot interface not being pythonic and that they prefer the OO interface.
 5. They might comment on the lack of units on the plot, and labelling, and maybe poor colorbar choice.
"""