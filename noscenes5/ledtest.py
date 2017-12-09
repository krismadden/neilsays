import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)

#print "LED on"
LEDon()
time.sleep(1)
#print "LED off"
LEDoff()

time.sleep(1)
LEDon()
time.sleep(1)
LEDoff()

time.sleep(1)
LEDon()
time.sleep(1)
LEDoff()

time.sleep(1)
LEDon()
time.sleep(1)
LEDoff()

time.sleep(1)
LEDon()
time.sleep(1)
LEDoff()

time.sleep(1)
LEDon()
time.sleep(1)
LEDoff()

time.sleep(1)
LEDon()
time.sleep(1)
LEDoff()



def LEDoff():
	GPIO.setup(21,GPIO.LOW)
	GPIO.setup(20,GPIO.LOW)
	GPIO.setup(16,GPIO.LOW)
	GPIO.setup(12,GPIO.LOW)
	GPIO.setup(7,GPIO.LOW)
	GPIO.setup(8,GPIO.LOW)
	GPIO.setup(25,GPIO.LOW)
	GPIO.setup(24,GPIO.LOW)
	GPIO.setup(23,GPIO.LOW)
	GPIO.setup(18,GPIO.LOW)
	GPIO.setup(15,GPIO.LOW)
	GPIO.setup(14,GPIO.LOW)

def LEDon():
	GPIO.setup(21,GPIO.HIGH)
	GPIO.setup(20,GPIO.HIGH)
	GPIO.setup(16,GPIO.HIGH)
	GPIO.setup(12,GPIO.HIGH)
	GPIO.setup(7,GPIO.HIGH)
	GPIO.setup(8,GPIO.HIGH)
	GPIO.setup(25,GPIO.HIGH)
	GPIO.setup(24,GPIO.HIGH)
	GPIO.setup(23,GPIO.HIGH)
	GPIO.setup(18,GPIO.HIGH)
	GPIO.setup(15,GPIO.HIGH)
	GPIO.setup(14,GPIO.HIGH)