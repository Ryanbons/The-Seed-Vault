from __future__ import print_function

import piplates.RELAYplate as RELAY
import time

ppADDR=0
RELAY.RESET(ppADDR)

rly = 1
t=10
st=0
for i in range(10):	
    RELAY.relayON(ppADDR,rly)
    time.sleep(t)
    st = st + t
    RELAY.relayOFF(ppADDR,rly)
    print("Time total: ",  st)
    time.sleep(3)


