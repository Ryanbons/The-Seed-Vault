from __future__ import print_function

import piplates.RELAYplate as RELAY
import time

ppADDR=0
RELAY.RESET(ppADDR)

vs = 0.00304
vo = -.0109
volt = 13.95
pump_windage2 = 14.0/16.0

ozs = raw_input("Enter oz to put out: ")
oz = float(ozs)
maxtime = float(raw_input("Enter time betwen nutrient doses: "))

print ("oz is: ", oz)

tp = oz/(volt*vs + vo) * pump_windage2

print ("tp is: ", tp)

N = tp/maxtime

tr = tp/(15*N)

print ("N: ", N)
print("tr: ", tr)

ontotal = 0
t = tp
RELAY.relayON(ppADDR, 1)
RELAY.relayON(ppADDR, 6)
RELAY.relayON(ppADDR, 7)

while True:
    RELAY.relayON(ppADDR, 2)
    print("pump 2 on")
    time.sleep(tr)
    RELAY.relayOFF(ppADDR, 2)
    ontotal = ontotal + tr
    print("pump 2 off")
    if t  < 0.0:
        break
    time.sleep(tp/N - tr)
    t = t - tp/N 
    print("t: ", t)

RELAY.relayOFF(ppADDR, 1)
RELAY.relayOFF(ppADDR, 6)
RELAY.relayOFF(ppADDR, 7)
print("ontotal: ", ontotal)




