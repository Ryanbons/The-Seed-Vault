from __future__ import print_function

import piplates.RELAYplate as RELAY
import piplates.DAQCplate as DAQC

import time

ppADDR=1
ADCchan=0
channel_name = {0:'pH', 1:'Water Pressure', 2:'EC', 3:'Optical Water Height', 4:'Water Level Low', 5:'Water Level High', 6: 'Accum Temp', 7:'Photo'}
slope = {0:3.26, 1:58.39, 2:1039.086, 3:1, 4:1, 5:1, 6:108.43, 7:1}
intercept = {0:-.3024, 1:-29.43, 2:1.7576, 3:0, 4:0, 5:0, 6:-135, 7:0}
units = {0:" ", 1:'psi', 2:'PPM TDS', 3:'(digital)', 4:'(digital)', 5:'(digital)', 6:'Deg F', 7:'xxx'}

while True:
    adcread = DAQC.getADC(ppADDR, ADCchan)
    real_val = adcread * slope[ADCchan] + intercept[ADCchan]
    print("ADC reading #, name, val: ", ADCchan, channel_name[ADCchan], adcread, real_val, units[ADCchan])
    time.sleep(1.0)
    ADCchan = ADCchan + 1
    if ADCchan > 7:
        ADCchan = 0
        print('-------------------------------------------')






