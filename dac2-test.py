from __future__ import print_function

import piplates.RELAYplate as RELAY
import piplates.DAQCplate as DAQC

import time

ppADDR=1
volt = 0.0
i=0
while True:
    if i > 6:
        i=0
    DAQC.setDOUTbit(1,i)
    time.sleep(0.5)
    DAQC.clrDOUTbit(1,i)
    time.sleep(0.5)
    i=i+1
