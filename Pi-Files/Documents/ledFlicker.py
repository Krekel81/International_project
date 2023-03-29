import RPi.GPIO as GPIO
import time
import random

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set pin 14 as an output pin
GPIO.setup(14, GPIO.OUT)

# Flicker the light 10 times
for i in range(10):
    # Generate a random on/off time between 0.1 and 0.5 seconds
    on_time = random.uniform(0.1, 0.5)
    off_time = random.uniform(0.1, 0.5)
    
    # Turn on the light
    GPIO.output(14, GPIO.HIGH)
    
    # Wait for a random amount of time
    time.sleep(on_time)
    
    # Turn off the light
    GPIO.output(14, GPIO.LOW)
    
    # Wait for another random amount of time
    time.sleep(off_time)

# Clean up GPIO pins
GPIO.cleanup()

