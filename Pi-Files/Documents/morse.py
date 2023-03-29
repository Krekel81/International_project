import RPi.GPIO as GPIO
import time


short_timeout = 0.2
long_timeout = 1
# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set pin 14 as an output pin
GPIO.setup(14, GPIO.OUT)

# Define Morse code dictionary
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

# Function to convert a string to Morse code
def text_to_morse(text):
    morse = ''
    for char in text.upper():
        if char in morse_dict:
            morse += morse_dict[char] + ' '
        else:
            morse += '/'
    return morse

# Function to blink the LED in Morse code
def blink_morse(morse):
    for char in morse:
        if char == '.':
            GPIO.output(14, GPIO.HIGH)
            time.sleep(short_timeout)
            GPIO.output(14, GPIO.LOW)
            time.sleep(0.1)
        elif char == '-':
            GPIO.output(14, GPIO.HIGH)
            time.sleep(long_timeout)
            GPIO.output(14, GPIO.LOW)
            time.sleep(0.1)
        elif char == ' ':
            time.sleep(1)
        elif char == '/':
            time.sleep(0.7)

# Get text input from user
text = input('Enter a message to display in Morse code: ')

# Convert text to Morse code
morse = text_to_morse(text)

# Blink LED in Morse code
blink_morse(morse)

# Clean up GPIO pins
GPIO.cleanup()

