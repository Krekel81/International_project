import RPi.GPIO as GPIO
import time
#Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
# Set pin 8 as an output pin
GPIO.setup(14, GPIO.OUT)
timeout = 0.1


while True:
    # Turn on the light connected to pin 8
    GPIO.output(14, GPIO.HIGH)

    # Wait for 5 seconds
    time.sleep(timeout)

    # Turn off the light connected to pin 8
    GPIO.output(14, GPIO.LOW)

    time.sleep(timeout)

# Clean up GPIO pins
GPIO.cleanup()