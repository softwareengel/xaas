import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)      #Setup Methode
GPIO.setwarnings(False)

class LED (object):
    '''
    Es soll eine Klasse entwickelt werden, mit welcher es möglich ist
    eine LED anzusteuern, die an einem der GPIO Pins des Raspberry Pis
    angeschlossen ist.Folgende Methoden sollen realisiert werden:
    • turnLEDOn()
    • turnLEDOff()
    • blinkLED(wiederholungen)
    Die LED soll die übergebene Anzahl an
    Wiederholungen blinken.
    '''



    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def turnOn(self):
        GPIO.output(self.pin, 1)

    def turnOff(self):
        GPIO.output(self.pin, 0)

    def blink(self, count):
        while(count > 0):
            self.turnOn()
            sleep(2)
            self.turnOff()
            sleep(2)
            count = count - 1


'''    Schalten Sie die LED für 5 Sekunden ein und lassen Sie sie im Anschluss 10 mal blinken.
'''

gruneLED = LED(4)

gruneLED.turnOn()
time.sleep(5)
gruneLED.turnOff()
for x in range(10):
    gruneLED.turnOn()
    time.sleep(0.2)
    gruneLED.turnOff()
    time.sleep(0.2)
    print (x) 

gruneLED.blink(10)