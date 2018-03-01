import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
servoPin=11
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin, 50)
pwm.start(7)
for i in range(0,180):
	DC=1./18.*(i)+2
	pwm.ChangeDutyCycle(DC)
	time.sleep(.05)
for i in range(180,0,-1):
	DC=1/18.*i+2
	pwm.ChangeDutyCycle(DC)
	time.sleep(.05)
pwm.stop()
GPIO.cleanup()