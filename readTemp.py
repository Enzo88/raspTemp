# requires RPi_I2C_driver.py
import RPi_I2C_driver
from time import *
import RPi.GPIO as GPIO
import dht11
import time, sys
import datetime

mylcd = RPi_I2C_driver.lcd()

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=17)

while True:
    try: 
        result = instance.read()
        if result.is_valid():        
            mylcd.lcd_display_string("Temp: "+str(result.temperature)+" C", 1)
            mylcd.lcd_display_string("Humidity: %"+ str(result.humidity), 2)
        time.sleep(2)
    except KeyboardInterrupt:                    
        mylcd.lcd_clear()
        mylcd.backlight(0)
        sys.exit()

