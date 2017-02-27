#!/usr/bin/env python

"""
write_sensor_data_to_netcdf.py
==============================

Writes some tabular data to a NetCDF file.
"""

# Imports
import time
from netCDF4 import Dataset
from datetime import datetime, timedelta
from netCDF4 import num2date, date2num
import numpy as np

# Prepare the data first
rows = """2014-03-06T14:20:28.147494 +023.9C
2014-03-06T14:20:28.849280 +024.0C
2014-03-06T14:20:38.769283 +024.0C
2014-03-06T14:20:48.688270 +024.1C
2014-03-06T14:20:58.608165 +024.1C
2014-03-06T14:21:08.528660 +024.2C
2014-03-06T14:21:18.447250 +024.3C
2014-03-06T14:21:28.367255 +024.3C
2014-03-06T14:21:38.288262 +024.3C
2014-03-06T14:21:48.208270 +024.2C""".split("\n")

variable_metadata = {
    "var_id": "temp",
    "long_name": "Temperature of sensor (K)",
    "units": "K",
    "standard_name": "air_temperature"}

global_metadata = {
    "Conventions": "CF-1.6",
    "institution": "Leeds Uni",
    "title": "My first CF-netCDF file",
    "history": "%s: Written with script: write_sensor_data_to_netcdf.py" % (datetime.now().strftime("%x %X"))}

def convert_time(tm):
    tm = datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f")
    return tm

def convert_temp(temp):
    value = temp.strip("+").strip("C").lstrip("0")
    return float(value) - 273.15

# Parse the data into python lists
times = []
temps = []

for row in rows:
    tm, temp = row.strip().split()
    times.append(convert_time(tm))
    temps.append(convert_temp(temp))

# Set reference time and convert datetime values to offset values from reference time
base_time = datetime(2014, 3, 6, 14, 20, 28)
time_values = []

for t in times:
    value = t - base_time
    ts = value.total_seconds()
    time_values.append(ts)

time_units = "seconds since 2014-03-06 14:20:28"

# Create the output file (NetCDF dataset)
output_file = "sensor_data.nc"
dataset = Dataset(output_file, "w", format='NETCDF4_CLASSIC')

# Create the time dimension - with unlimited length
time_dim = dataset.createDimension("time", None)

# Create the time variable
time_var = dataset.createVariable("time", np.float64, ("time",))
time_var[:] = time_values
time_var.units = time_units
time_var.standard_name = "time"
time_var.calendar = "standard"

# Create the temp variable
temp = dataset.createVariable("temp", np.float32, ("time",))
temp[:] = temps

# Set the variable attributes
for (attr, value) in variable_metadata.items():
    setattr(temp, attr, value)

# Set the global attributes
for (attr, value) in global_metadata.items():
    setattr(dataset, attr, value)

# Write the file
dataset.close()

print "Wrote: %s" % output_file
print "Try: ncdump %s" % output_file
