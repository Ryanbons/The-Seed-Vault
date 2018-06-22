from __future__ import print_function

import piplates.RELAYplate as RELAY
import piplates.DAQCplate as DAQC

import time

ppADDR=1
ADCchan=0

print('reading adc channel', ADCchan)

while True:
    adcread = DAQC.getADC(ppADDR, ADCchan)
    print("ADC reading #, val: ", ADCchan, adcread)
    time.sleep(1.0)
    ADCchan = ADCchan + 1
    if ADCchan > 7:
        ADCchan = 0





