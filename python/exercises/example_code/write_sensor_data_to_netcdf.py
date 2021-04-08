#!/usr/bin/python2.7

"""
write_sensor_data_to_netcdf-dw.py
==============================

Writes some tabular data to a NetCDF file.
"""

# Imports
import time
from netCDF4 import Dataset
from datetime import datetime, timedelta
import numpy as np

#grab data from infile
INFILE='../example_data/sample-serial-temperature-2h.tsv'
from csv import reader

#functions to convert from text file format to 
#numbers
def convert_time(tm):
    tm = datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f")
    return tm

def convert_temp(temp):
    value = temp.strip("+").strip("C").lstrip("0")
    return float(value) + 273.15

# Parse the data into python lists
times = []
temps = []

#open infile and read data into lists
with open(INFILE, 'rt') as tsvfile:
   tsvreader = reader(tsvfile, delimiter='\t')
   for row in tsvreader:
      times.append(convert_time(row[0]))
      temps.append(convert_temp(row[1]))

# Set reference time and convert datetime values to offset values from reference time
#reference time is the first time in the input data
base_time = times[0]
time_values = []

for t in times:
    value = t - base_time
    ts = value.total_seconds()
    time_values.append(ts)

time_units = "seconds since " + base_time.strftime('%Y-%m-%d %H:%M:%S')

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

#  Set   the   variable attributes
temp.var_id =  "temp"   
temp.long_name =  "Temperature   of sensor   (K)"  
temp.units  =  "K"   
temp.standard_name   =  "air_temperature" 
#  Set   the   global   attributes
dataset.Conventions  =  "CF-1.6" 
dataset.institution  =  "NCAS"   
dataset.title  =  "My   first CF-netCDF   file" 
dataset.history   =  "%s:  Written  with  script:  write_sensor_data_to_netcdf.py"  %  (datetime.now().strftime("%x  %X"))

# Write the file
dataset.close()

print("Wrote: %s" % output_file)
print("Try: ncdump %s" % output_file)
