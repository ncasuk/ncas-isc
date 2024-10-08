from netCDF4 import Dataset
import numpy as np

# Set up data to put in
dataset = Dataset("../example_data/ggas2014121200_00-18.nc", "r", format="NETCDF4_CLASSIC")
sst = dataset.variables["SSTK"]
arr = sst[1, 0, 10:20, 30:35]
vars = dataset.variables
arr_time = vars["time"][1]
arr_level = vars["surface"][0]
arr_lats = vars["latitude"][10:20]
arr_lons = vars["longitude"][30:35]
metadata = {}
for attr in sst.ncattrs():
    metadata[attr] = getattr(sst, attr)

myds = Dataset('mydata.nc', 'w', format='NETCDF4_CLASSIC')

time = myds.createDimension('time', 1)
level = myds.createDimension('level', 1)
lat = myds.createDimension('lat', 10)
lon = myds.createDimension('lon', 5)

times = myds.createVariable('time', np.float64, ('time',))
levels = myds.createVariable('level', np.int32, ('level',))
latitudes = myds.createVariable('latitude', np.float32,
 ('lat',))
longitudes = myds.createVariable('longitude', np.float32,
 ('lon',))

myvar = myds.createVariable('temp', np.float32,
 ('time','level','lat','lon'))

del metadata["_FillValue"]

for (key, value) in metadata.items():
    myvar.setncattr(key, value)

myds.source = "super dataset"

times[:] = arr_time
levels[:] = arr_level
latitudes[:] = arr_lats
longitudes[:] = arr_lons


myvar[:] = arr

myds.close()

