#!/user/bin/python
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)

# temp_log.py


import os, time
os.system('modprobe wire')
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')



PFAD = '/sys/bus/w1/devices/10-00080341bd68/w1_slave'
PFD = '/sys/bus/w1/devices/28-0316a13a79ff/w1_slave'
def readTemp():
    ok = False
    while not ok:
        f = open(PFAD, 'r')
        zeile_1 = f.readline()             
        zeile_2 = f.readline()
        f.close()
        if 'YES' in zeile_1:
            ok = True
    teil_1, teil_2 = zeile_2.split('=')
    return int(teil_2)/100

def readTem():
    ok = False
    while not ok:
        op = open(PFD, 'r')
        zeile_1 = op.readline()             
        zeile_2 = op.readline()
        op.close()
        if 'YES' in zeile_1:
            ok = True
    teil_1, teil_2 = zeile_2.split('=')
    return int(teil_2)/100


# Hauptprogramm
from time import asctime
i = 0
speicher = open('messung1.cvs', 'w')
print('Stunden; Temperatur außen in °C; Temperatur innen in °C', file=sp, 
      flush=True)
time.sleep(180)
while True:
    t = asctime()
    e = round(readTemp())
    a = round(readTem())
    print(t,';',a,';',e, file=speicher, flush=True)
    time.sleep(1200)
