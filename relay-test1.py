from __future__ import print_function

import piplates.RELAYplate as RELAY
import time

ppADDR=1
RELAY.RESET(ppADDR)

rly = 2

while True:
    print('rly: ', rly)

    RELAY.relayON(ppADDR,rly)
    print('on')
    time.sleep(1)
    RELAY.relayOFF(ppADDR,rly)
    print('off')
    time.sleep(1)
    rly = rly + 1
    if rly > 7:
        rly = 2



