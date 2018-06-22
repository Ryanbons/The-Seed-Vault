from __future__ import print_function

import piplates.RELAYplate as RELAY
import piplates.DAQCplate as DAQC

import time

ppADDR=1
volt = 0.0
i=0
while True:
    if volt >= 4.095:
        volt = 0.0
    if i > 6:
        i=0
    DAQC.setDAC(1, 0, volt)
    DAQC.setDOUTbit(1,i)
    time.sleep(0.1)
    volt = volt + .01
    i=i+1
