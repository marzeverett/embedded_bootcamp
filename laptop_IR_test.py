import time
import serial

#com_port = 'COM0'
#com_port = '/dev/ttyACM0'
com_port = '/dev/ttyUSB0'


arduino = serial.Serial(port=com_port, baudrate=9600, timeout=0.1)
 

def main():
    while(1):
        #Read in a message
        data = arduino.readline()
        message = data.decode()
        #If any button press 
        if len(message) > 1:
            print(message)
            print(type(message))

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass 



