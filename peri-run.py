from __future__ import print_function

import piplates.RELAYplate as RELAY
import time

ppADDR=0
RELAY.RESET(ppADDR)

vs = 0.00304
vo = -.0109
volt = 11.99

ozs = raw_input("Enter oz to put out: ")
oz = float(ozs)

print ("oz is: ", oz)

t = oz/(volt*vs + vo)

print ("t is: ", t)

rly = 1

RELAY.relayON(ppADDR,rly)
time.sleep(t)
RELAY.relayOFF(ppADDR,rly)


