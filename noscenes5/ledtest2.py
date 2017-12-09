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

def Loff(pin):
	GPIO.setup(pin,GPIO.LOW)

def Lon(pin):
	GPIO.setup(pin,GPIO.HIGH)

Lon(21)
time.sleep(1)
Loff(21)

Lon(20)
time.sleep(1)
Loff(20)

Lon(16)
time.sleep(1)
Loff(16)

Lon(12)
time.sleep(1)
Loff(12)

Lon(7)
time.sleep(1)
Loff(7)

Lon(8)
time.sleep(1)
Loff(8)

Lon(25)
time.sleep(1)
Loff(25)

Lon(24)
time.sleep(1)
Loff(24)

Lon(23)
time.sleep(1)
Loff(23)

Lon(18)
time.sleep(1)
Loff(18)

Lon(15)
time.sleep(1)
Loff(15)

Lon(14)
time.sleep(1)
Loff(14)


Lon(21)
time.sleep(1)
Loff(21)

Lon(20)
time.sleep(1)
Loff(20)

Lon(16)
time.sleep(1)
Loff(16)

Lon(12)
time.sleep(1)
Loff(12)

Lon(7)
time.sleep(1)
Loff(7)

Lon(8)
time.sleep(1)
Loff(8)

Lon(25)
time.sleep(1)
Loff(25)

Lon(24)
time.sleep(1)
Loff(24)

Lon(23)
time.sleep(1)
Loff(23)

Lon(18)
time.sleep(1)
Loff(18)

Lon(15)
time.sleep(1)
Loff(15)

Lon(14)
time.sleep(1)
Loff(14)

Lon(21)
time.sleep(1)
Loff(21)

Lon(20)
time.sleep(1)
Loff(20)

Lon(16)
time.sleep(1)
Loff(16)

Lon(12)
time.sleep(1)
Loff(12)

Lon(7)
time.sleep(1)
Loff(7)

Lon(8)
time.sleep(1)
Loff(8)

Lon(25)
time.sleep(1)
Loff(25)

Lon(24)
time.sleep(1)
Loff(24)

Lon(23)
time.sleep(1)
Loff(23)

Lon(18)
time.sleep(1)
Loff(18)

Lon(15)
time.sleep(1)
Loff(15)

Lon(14)
time.sleep(1)
Loff(14)
