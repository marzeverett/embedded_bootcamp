import time
import RPi.GPIO as GPIO 

#https://projects.raspberrypi.org/en/projects/grandpa-scarer/3

GPIO.setmode(GPIO.BOARD)



#Pin 17 
GPIO.setup(11, GPIO.OUT)
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
        action()
        time.sleep(1)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()




