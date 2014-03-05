#!/usr/bin/env python

from datetime import datetime
import serial, io

ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
)

#To use python's readline detection in python v2.6 or later 
#you need to wrap the Serial instance
#( http://pyserial.sourceforge.net/shortintro.html#readline )

#The Papouch temp probe uses carriage returns (ascii 13 or "\r" in python[1]) so specify
# TextIOWrapper's default "universal newlines" mode also works, but the Serial module's
# readline does not.
# http://docs.python.org/2/glossary.html#term-universal-newlines
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')
    
while ser.isOpen():                
   print datetime.utcnow().isoformat(), sio.readline() 

ser.close


# 1. \r for carriage return is standard notation (an 'escape sequence') 
#    in many programming languages including Python and C. 
#    \n would be ascii 11, a newline.
