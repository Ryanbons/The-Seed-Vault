from __future__ import print_function
### 
import piplates.RELAYplate as RELAY
import time
import datetime
import sys

if len(sys.argv) < 2:
    print('Usage: python mist-cycle.py <period> <time> (in seconds)')
    print('Using default period 60 secs, default mist time 1 sec')
    mist_period = 60.0
    mist_time = 0.4
else:
    mist_period = float(sys.argv[1])
    mist_time = float(sys.argv[2])

print('Mist period: ', mist_period)
print('Mist time: ', mist_time)


ppADDR=0

#RELAY.RESET(ppADDR)

#rly = 7
#RELAY.relayON(ppADDR,rly)
#print('relay 7 is on')
#time.sleep(1)


print('starting spray loop')
while True:
    rly = 6
    RELAY.relayON(ppADDR,rly)
    print('Time: ', datetime.datetime.now())
    print('Spray on')
    time.sleep(mist_time)
    RELAY.relayOFF(ppADDR,rly)
    print('Spray off, sleeping')
    time.sleep(mist_period)


