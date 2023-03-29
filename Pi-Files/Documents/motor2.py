import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
motor1_a = 14
motor1_b = 15
motor2_a = 18
motor2_b = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_a, GPIO.OUT)
GPIO.setup(motor1_b, GPIO.OUT)
GPIO.setup(motor2_a, GPIO.OUT)
GPIO.setup(motor2_b, GPIO.OUT)


# Define functions to control the motors
def motor1_forward():
    GPIO.output(motor1_a, GPIO.HIGH)
    GPIO.output(motor1_b, GPIO.LOW)

def motor1_backward():
    GPIO.output(motor1_a, GPIO.LOW)
    GPIO.output(motor1_b, GPIO.HIGH)

def motor1_stop():
    GPIO.output(motor1_a, GPIO.LOW)
    GPIO.output(motor1_b, GPIO.LOW)

def motor2_forward():
    GPIO.output(motor2_a, GPIO.HIGH)
    GPIO.output(motor2_b, GPIO.LOW)

def motor2_backward():
    GPIO.output(motor2_a, GPIO.LOW)
    GPIO.output(motor2_b, GPIO.HIGH)

def motor2_stop():
    GPIO.output(motor2_a, GPIO.LOW)
    GPIO.output(motor2_b, GPIO.LOW)

# Test the motors
motor1_forward()
print("motor1 forward")
motor2_forward()
print("motor2 forward")
time.sleep(4)
motor1_stop()
print("motor1 stop")
motor2_stop()
print("motor2 stop")
time.sleep(4)
motor1_backward()
print("motor1 backward")
motor2_backward()
print("motor2 backward")
time.sleep(4)
motor1_stop()
print("motor1 stop")
motor2_stop()
print("motor2 stop")

# Clean up the GPIO pins
GPIO.cleanup()
