import bluetooth
import serial

port = serial.Serial('/dev/rfcomm0', baudrate=9600)
while True:
    data = port.readline().decode('utf-8')
    print(data)
