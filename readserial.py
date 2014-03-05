#!/usr/bin/env python

import time
import serial

ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
)
                    
print ser.readline()
ser.close
