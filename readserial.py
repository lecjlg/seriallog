#!/usr/bin/env python

import time
import serial

ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
)
                    
#print ser.readline() #temp probe returns Carriage return as newline, so this does not work
print ser.read(size=8) # all its returns are eight characters
ser.close
