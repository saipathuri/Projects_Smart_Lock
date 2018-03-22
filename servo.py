import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
servoPin=8
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin, 50)
pwm.start(7)

def lock():
	DC=1./18.*(180)+2
	pwm.ChangeDutyCycle(DC)
	return True

def unlock():
	DC=1/18.*(90)+2
	pwm.ChangeDutyCycle(DC)
	sleep(.05)
	return True

def clean_up():
	pwm.stop()
	GPIO.cleanup()
