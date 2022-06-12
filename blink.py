import RPi.GPIO as GPIO
import time

ledPin = 11

def ledSetup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    print("Pin%d is now active")

def ledLoop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        print("LED Turned ON")
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        print("LED Turned OFF")
        time.sleep(1)

def endProcess():
    GPIO.cleanup()

if __name__ == "__main__":
    print("LED Program is Starting Now... \n")
    ledSetup()
    try:
        ledLoop()
    except KeyboardInterrupt:
        endProcess()