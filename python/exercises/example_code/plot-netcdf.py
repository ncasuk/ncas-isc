#!/usr/bin/python2.7

''' Plots a line graph from a NetCDF file '''

from netCDF4 import Dataset, num2date
import numpy as np
import matplotlib.pyplot as plt

# Tick "locators" c.f. http://matplotlib.org/api/dates_api.html
from matplotlib.dates import MinuteLocator, DateFormatter

datafile = 'sensor_data.nc'

nc = Dataset(datafile, mode='r')

temp = nc.variables['temp']
temps = temp[:]
time = nc.variables['time']
times = []
times = num2date(list(time[:]),units=time.units, calendar=time.calendar)

#get "handles" to affect plot styling
fig, ax = plt.subplots()
#tick every tenth minute
ax.xaxis.set_major_locator(MinuteLocator(byminute=range(0,60,10)))

#format of date on x-axis (display minutes, uses strftime)
ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))


#tick every minute
ax.xaxis.set_minor_locator(MinuteLocator())
ax.autoscale_view()

#line graph
plt.plot_date(times,temps,'-')
labels = ax.get_xticklabels()
plt.setp(labels, rotation=90, fontsize=10, horizontalalignment='center')
plt.xlabel(time.standard_name)
plt.ylabel(temp.standard_name + ' / ' + temp.units)
plt.title(nc.title)

#tidy up layout automatically
fig.tight_layout()

plt.savefig('sensor_data.png')
