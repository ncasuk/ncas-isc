#!/usr/bin/env python
from datetime import datetime
import serial
import io

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
)


print(datetime.utcnow().strftime('%H:%M:%S'), ser.read(8))
print(datetime.utcnow().strftime('%H:%M:%S'), ser.read(8))

print("")

datastring = ser.read(8)
print(datetime.utcnow().strftime('%H:%M:%S'), datastring)
datastring = ser.read(8)
print(datetime.utcnow().strftime('%H:%M:%S'), datastring)

ser.close()
