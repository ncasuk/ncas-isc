from netCDF4 import Dataset
import numpy as np
import time as mytime
from numpy.random import uniform
from datetime import datetime, timedelta
from netCDF4 import num2date, date2num

# Open file
dataset = Dataset('test.nc', 'w', format='NETCDF4_CLASSIC')

# Create dimensions
longitude = dataset.createDimension('longitude', 144)
latitude = dataset.createDimension('latitude', 73)
level = dataset.createDimension('level', 10)
time = dataset.createDimension('time', None)

# Create coordinate variables for 4-dimensions
times = dataset.createVariable('time', np.float64, ('time',)) 
levels = dataset.createVariable('level', np.int32, ('level',)) 
latitudes = dataset.createVariable('latitude', np.float32, ('latitude',))
longitudes = dataset.createVariable('longitude', np.float32, ('longitude',)) 

# Create the actual 4-d variable
temp = dataset.createVariable('temp', np.float32, ('time','level','latitude','longitude'))

# Global Attributes
dataset.description = 'bogus example script' 
dataset.history = 'Created ' + mytime.ctime(mytime.time()) 
dataset.source = 'netCDF4 python module tutorial'

#Assign variable attributes
longitudes.standard_name='longitude'
longitudes.units = 'degree_east'
latitudes.standard_name='latitude'
latitudes.units = 'degree_north' 
levels.standard_name='pressure'
levels.units = 'hPa'
times.standard_name='time'
times.units = 'hours since 0001-01-01 00:00:00' 
times.calendar = 'gregorian'
temp.standard_name='air_temperature'
temp.units = 'K'

# Writing data
longitudes[:] = np.arange(-180,180,2.5)
latitudes[:] = np.arange(-90,91,2.5)
levels[:] = [1000, 900, 700, 500, 300, 100, 70, 50, 30, 10]
temp[0:5,:,:,:] = uniform(size=(5,10,73,144))

# Fill in times
dates = []
for n in range(5):
    dates.append(datetime(2001, 3, 1) + n * timedelta(hours=12))

times[:] = date2num(dates, units = times.units, calendar = times.calendar)

# Close file
dataset.close()
