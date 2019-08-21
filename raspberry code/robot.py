import RPi.GPIO as GPIO
import time

def init():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)


        global prawy
        global lewy

        prawy= GPIO.PWM(17, 90)
        lewy= GPIO.PWM(27, 90)
        prawy.start(0)
        lewy.start(0)

def null():
        global prawy
        global lewy
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        prawy.ChangeDutyCycle(0)
        lewy.ChangeDutyCycle(0)


def rightUp(procent):
        global prawy
        global lewy
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
        prawy.ChangeDutyCycle(100)
        lewy.ChangeDutyCycle(procent)



def leftUp(procent):
        global prawy
        global lewy
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
        prawy.ChangeDutyCycle(procent)
        lewy.ChangeDutyCycle(100)


def rightDown(procent):
        global prawy
        global lewy
        GPIO.output(13,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        prawy.ChangeDutyCycle(100)
        lewy.ChangeDutyCycle(procent)


def leftDown(procent):
        global prawy
        global lewy
        GPIO.output(13,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
        prawy.ChangeDutyCycle(procent)
        lewy.ChangeDutyCycle(100)


def close():
        global prawy
        global lewy
        prawy.stop()
        lewy.stop()
        GPIO.output(13,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
        GPIO.cleanup()
