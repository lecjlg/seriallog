#!/usr/bin/env python

from datetime import datetime
import serial, io

ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
)

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')
    
while ser.isOpen():                
   datastring = sio.readline()
   print datetime.utcnow().isoformat(), datastring

ser.close()
