#!/usr/bin/env python

from datetime import datetime
import serial

ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
)
                    
#print ser.readline() #temp probe returns Carriage return as newline, so this does not work
print datetime.utcnow().isoformat(), ser.read(size=8) # all its returns are eight characters

ser.close()
