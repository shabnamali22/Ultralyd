from hcsr04 import HCSR04
from time import sleep

#opretter instans af HCSR04 klassen
sensor = HCSR04(15,34)
#starter event loop
while True:
    #Klader distance_cm metoden og gemmer returværdien i variablen distance
    distance = sensor.distance_cm()
    print("Distance:" , distance,"cm")
    sleep(1)