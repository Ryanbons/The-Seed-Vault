from __future__ import print_function

import piplates.RELAYplate as RELAY
import piplates.DAQCplate as DAQC

import time

ppADDR=1
adADDR=1

cooler_rly = 7
ADCchan = 6
temp_slope = 108.43
temp_inter = -135
temp_setpoint = 67.0
temp_hyster = 4.0

try:
    while True:

        adcread = DAQC.getADC(adADDR, ADCchan)
        print('Temp voltage: ', adcread)

        temp_val = adcread * temp_slope + temp_inter
        print('Temp: ', temp_val)

        if temp_val > temp_setpoint+temp_hyster:
            RELAY.relayON(ppADDR,cooler_rly)
            print('Cooling')

        if temp_val <= temp_setpoint:
            RELAY.relayOFF(ppADDR,cooler_rly)
            print('Optimal Temperature Achieved')

        time.sleep(10)
except KeyboardInterrupt:
    print('Caught ^C')
    RELAY.relayOFF(ppADDR, cooler_rly)
    exit()



