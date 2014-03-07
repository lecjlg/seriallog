#!/usr/bin/env python
'''This version of the readserial program demonstrates using python to write 
an output file'''

from datetime import datetime
import serial, io

outfile='/tmp/serial-temperature.tsv'

ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')

with open(outfile,'a') as f: #appends to existing file 
   while ser.isOpen():
      datastring = sio.readline()
      #tab-separated
      #print datetime.utcnow().isoformat() + '\t' + datastring + '\n'
      f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n') # \n is line separator
      #f.flush() #included to force the system to write to disk

ser.close()
