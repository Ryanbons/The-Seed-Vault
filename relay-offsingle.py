from __future__ import print_function

import piplates.RELAYplate as RELAY
import time
import sys

if len(sys.argv) < 2:
    print('Usage: python relay-offsingle.py <n> <m> for board n, relay m)')
    print('Exiting')
    exit()
else:
    ppADDR = int(sys.argv[1])
    rly= int(sys.argv[2])

if ppADDR < 0 or ppADDR >1:
    print('Error - bad ppADDR')
    exit()

if rly < 0 or rly > 7:
    print('Error - bad rly')
    exit()

print('ppADDR: ', ppADDR)
print('rly: ', rly)

RELAY.relayOFF(ppADDR,rly)




