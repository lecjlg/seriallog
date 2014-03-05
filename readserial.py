#! python

import time
import serial
import time

ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
)
                    
print ser.readline()
ser.close
