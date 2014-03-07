#!/usr/bin/env python

from datetime import datetime
import serial

ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
)

#flush input buffer

datastring = ser.read(size=8)
print datetime.utcnow().isoformat(), datastring

ser.close()
