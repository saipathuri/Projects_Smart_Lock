import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
servoPin=14
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin, 50)
pwm.start(7)

def lock():
	for i in range(0,180):
		DC=1./18.*(i)+2
		pwm.ChangeDutyCycle(DC)
		time.sleep(.05)
	return True

def lock_open():
	for i in range(180,0,-1):
		DC=1/18.*i+2
		pwm.ChangeDutyCycle(DC)
		time.sleep(.05)
	return True

def clean_up():
	pwm.stop()
	GPIO.cleanup()
