import RPi.GPIO as GPIO
import time

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

GPIO.output(motor1_a, GPIO.LOW)
GPIO.output(motor1_b, GPIO.LOW)
GPIO.output(motor1_a, GPIO.LOW)
GPIO.output(motor1_b, GPIO.LOW)
GPIO.output(motor2_a, GPIO.LOW)
GPIO.output(motor2_b, GPIO.LOW)
GPIO.output(motor2_a, GPIO.LOW)
GPIO.output(motor2_b, GPIO.LOW)
pwm1.ChangeDutyCycle(0)
pwm2.ChangeDutyCycle(0)

GPIO.cleanup()