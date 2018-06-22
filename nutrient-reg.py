from __future__ import print_function

import piplates.RELAYplate as RELAY
import piplates.DAQCplate as DAQC

import time

ppADDR=0
adADDR=1

RELAY.RESET(ppADDR)

nutrients_rly = 2
mixmotor_rly = 5
ADCchan = 2
eC_slope = 1039.086
eC_inter = 1.7576
eC_setpoint = 100
eC_hyster = 20.0

while True:

    adcread = DAQC.getADC(adADDR, ADCchan)
    print('eC Voltage: ', adcread)

    eC_val = adcread * eC_slope + eC_inter
    print('eC: ', eC_val)

    if eC_val < eC_setpoint-eC_hyster:
       RELAY.relayON(ppADDR,mixmotor_rly)
       time.sleep(10)
       RELAY.relayON(ppADDR,nutrients_rly)
       time.sleep(1)
       RELAY.relayOFF(ppADDR,nutrients_rly)
       print('Adding Nutrients')

    if eC_val >= eC_setpoint:
       RELAY.relayOFF(ppADDR,nutrients_rly)
       time.sleep(10)
       RELAY.relayOFF(ppADDR,mixmotor_rly)
       print('Optimal Nutrient Level Achieved')

    time.sleep(10)



