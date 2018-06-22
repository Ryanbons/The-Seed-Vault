from __future__ import print_function

import piplates.RELAYplate as RELAY
import piplates.DAQCplate as DAQC

import time

ppADDR=0
adADDR=1

RELAY.RESET(ppADDR)

pump_rly = 1
pump_solenoid = 7
ADCchan = 1
psi_slope = 58.39
psi_inter = -29.43
psi_setpoint = 120.0
psi_hyster = 40.0
psi_MAX = 160.0
psi_MIN = 0.0

while True:

    adcread = DAQC.getADC(adADDR, ADCchan)
    print('PSI voltage: ', adcread)

    psi_val = adcread * psi_slope + psi_inter
    print('PSI: ', psi_val)

    if psi_val < psi_MIN or psi_val > psi_MAX:
        time.sleep(.5)
        continue

    if psi_val < psi_setpoint-psi_hyster:
       RELAY.relayON(ppADDR,pump_solenoid)
       RELAY.relayON(ppADDR,pump_rly)
       print('Pump and solenoids on')

    if psi_val >= psi_setpoint:
        RELAY.relayOFF(ppADDR,pump_rly)
        RELAY.relayOFF(ppADDR,pump_solenoid)
        print('Pump and solenoid off')


    time.sleep(.2)



