from utime import sleep
from machine import Pin

print("Hello World!")

led = Pin(15, Pin.OUT)
while True:
    led.on()
    print("Led ON, Ligado!")
    sleep(0.5)
    led.off()
    print("Led OFF, Desligado!")