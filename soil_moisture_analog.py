import RPi.GPIO as GPIO
import time

# Define GPIO pins
RD_PIN = 23
WR_PIN = 22
DATA_PINS = [4, 17, 27, 10, 5, 6, 13, 19]  # D0-D7

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RD_PIN, GPIO.OUT)
GPIO.setup(WR_PIN, GPIO.OUT)
for pin in DATA_PINS:
    GPIO.setup(pin, GPIO.IN)

def read_adc():
    GPIO.output(WR_PIN, GPIO.LOW)
    time.sleep(0.0001)  # Short delay
    GPIO.output(WR_PIN, GPIO.HIGH)
    
    time.sleep(0.0001)  # Allow time for conversion
    GPIO.output(RD_PIN, GPIO.LOW)
    
    value = 0
    for i, pin in enumerate(DATA_PINS):
        if GPIO.input(pin):
            value |= (1 << i)
    
    GPIO.output(RD_PIN, GPIO.HIGH)
    return value

try:
    while True:
        adc_value = read_adc()
        print("ADC Value:", adc_value)
        time.sleep(1)
finally:
    GPIO.cleanup()
