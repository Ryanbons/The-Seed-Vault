import RPi.GPIO as GPIO
import time
import piplates.RELAYplate as RELAY

GPIO.setmode(GPIO.BCM)

ppADDR=0

RELAY.RESET(ppADDR)

TRIG = 16
ECHO = 20

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
idist = 1
sumdist = 0.0
DIST_AVG = 5     # number of readings to average per reading
LOW_WATER = 15   # specified in cm below ultrasonic sensor
HIGH_WATER = 10  # specified in cm below ultrasonic sensor


while True:
    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(.5)

    GPIO.output(TRIG, True)
    time.sleep(0.000020)
    GPIO.output(TRIG, False)

    time.sleep(.000020)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    # print ("pulse end: ", pulse_end)
    # print ("pulse start: ", pulse_start)

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    sumdist = sumdist + distance
    idist = idist + 1
    if idist < DIST_AVG:
       continue
    else:
       dist = sumdist/float(DIST_AVG)
       print "Distance:",dist,"cm"
       if dist > LOW_WATER:
           pass
           # RELAY.relayON(ppADDR, 1)
       if dist < HIGH_WATER:
           pass
           # RELAY.relayOFF(ppADDR, 1)
       idist = 1
       sumdist = 0

GPIO.cleanup()
