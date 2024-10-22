import time
import serial
import RPi.GPIO as GPIO 

#https://projects.raspberrypi.org/en/projects/grandpa-scarer/3

GPIO.setmode(GPIO.Board)

#com_port = 'COM0'
#com_port = '/dev/ttyACM0'
com_port = '/dev/ttyUSB0'


#Pin 17 
GPIO.setup(11, GPIO.OUT)
arduino = serial.Serial(port=com_port, baudrate=9600, timeout=0.1)
#Setup pin 11 
p = GPIO.PWM(11,50) 


def action():
    p.start(0)
    p.ChangeDutyCycle(3)
    time.sleep(1)
    p.ChangeDutyCycle(12)
    time.sleep(1)
    p.stop()

def main():
    while(1):
        #Read in a message
        data = arduino.readline()
        print(data)
        message = data.decode()
        #If any button press 
        if len(message) > 1:
            print(message)
            print(type(message))
            action()

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()




