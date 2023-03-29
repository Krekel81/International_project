import RPi.GPIO as GPIO
import time

# set GPIO mode and pin number
GPIO.setmode(GPIO.BCM)
LED_PIN = 14

# set up LED pin as output
GPIO.setup(LED_PIN, GPIO.OUT)

# create PWM object and set initial frequency and duty cycle
pwm = GPIO.PWM(LED_PIN, 1000)  # frequency = 1000 Hz
pwm.start(0)  # duty cycle = 0%

# flicker LED
while True:
    for dc in range(0, 101, 5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.05)
    for dc in range(100, -1, -5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.05)

# cleanup GPIO
pwm.stop()
GPIO.cleanup()

