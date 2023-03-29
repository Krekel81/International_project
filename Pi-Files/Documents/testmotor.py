import RPi.GPIO as GPIO
import time
import sys

speed = int(input("Give me the speed of the car (25 | 50 | 75 | 100)\n"))
timeout = float(input("Give me the timeout between forward and backwards in seconds\n"))
if speed != 25 or speed != 50 or speed != 75 or speed != 100:
    speed = 50
if timeout < 0.1:
    timeout = 2 
# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for L298N H-bridge
motor1_a = 14
motor1_b = 15
motor1_e = 24
motor2_a = 18
motor2_b = 23
motor2_e = 25

# Set GPIO pins as output
GPIO.setup(motor1_a, GPIO.OUT)
GPIO.setup(motor1_b, GPIO.OUT)
GPIO.setup(motor1_e, GPIO.OUT)
GPIO.setup(motor2_a, GPIO.OUT)
GPIO.setup(motor2_b, GPIO.OUT)
GPIO.setup(motor2_e, GPIO.OUT)

# Create PWM objects for motor enable pins
pwm1 = GPIO.PWM(motor1_e, 100)
pwm2 = GPIO.PWM(motor2_e, 100)

# Start PWM
pwm1.start(0)
pwm2.start(0)

# Define motor control functions
def motor1_reverse(speed):
    GPIO.output(motor1_a, GPIO.HIGH)
    GPIO.output(motor1_b, GPIO.LOW)
    pwm1.ChangeDutyCycle(speed)

def motor1_forward(speed):
    GPIO.output(motor1_a, GPIO.LOW)
    GPIO.output(motor1_b, GPIO.HIGH)
    pwm1.ChangeDutyCycle(speed)

def motor2_reverse(speed):
    GPIO.output(motor2_a, GPIO.LOW)
    GPIO.output(motor2_b, GPIO.HIGH)
    pwm2.ChangeDutyCycle(speed)

def motor2_forward(speed):
    GPIO.output(motor2_a, GPIO.HIGH)
    GPIO.output(motor2_b, GPIO.LOW)
    pwm2.ChangeDutyCycle(speed)

# Set motors to stop initially
pwm1.ChangeDutyCycle(0)
pwm2.ChangeDutyCycle(0)

try:
    # Control motors
    motor1_forward(speed)  # set motor 1 to go forward at 50% speed
    motor2_forward(speed)  # set motor 2 to go backward at 25% speed
    time.sleep(timeout)       # wait 2 seconds
    motor1_reverse(speed)  # set motor 1 to go backward at 75% speed
    motor2_reverse(speed) # set motor 2 to go forward at 100% speed
    time.sleep(timeout)       # wait 2 seconds
    GPIO.cleanup()

except KeyboardInterrupt:
    # Clean up GPIO pins
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

