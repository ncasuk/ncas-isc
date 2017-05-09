from netCDF4 import Dataset
import numpy as np

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
    setattr(myvar, key, value)

myds.source = "super dataset"

times[:] = [0]
levels[:] = [0]
latitudes[:] = range(10)
longitudes[:] = range(5)


myvar[:] = arr

myds.close()

