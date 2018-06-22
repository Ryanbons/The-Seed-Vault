from __future__ import print_function

import piplates.RELAYplate as RELAY
import time

ppADDR=0
RELAY.RESET(ppADDR)

rly = 6
RELAY.relayON(ppADDR,rly)
print('relay 6 is on')
time.sleep(1)


print('starting spray loop')
while True:
    rly = 7
    RELAY.relayON(ppADDR,rly)
    print('Spray on, sleeping 1 sec')
    time.sleep(1)
    RELAY.relayOFF(ppADDR,rly)
    print('Spray off, sleeping  10 secs')
    time.sleep(10)


