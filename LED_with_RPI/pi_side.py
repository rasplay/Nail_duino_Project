# Including Library
import RPi.GPIO as GPIO
import time
import serial

# Define Serial Variables
DEFAULT_BAUDRATE = 9600
DEVICE = "/dev/ttyAMA0"

# Define Using PinNo and Other Variables
LED_PIN = 23

# Initializing Serial Port
port = serial.Serial(DEVICE, baudrate=DEFAULT_BAUDRATE)

# looping program
while(True):
    # On
    port.write('1')
    # Sleep
    time.sleep(1)
    print 'on'
    # Off
    port.write('0')
    # Sleep
    time.sleep(1)
