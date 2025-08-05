import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for fan and pump
FAN_PIN = 17
PUMP_PIN = 18

# Set up GPIO pins as outputs
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.setup(PUMP_PIN, GPIO.OUT)

# Function to turn fan on
def fan_on():
    GPIO.output(FAN_PIN, GPIO.LOW)  # Assuming LOW triggers relay ON
    print("Fan is ON")

# Function to turn fan off
def fan_off():
    GPIO.output(FAN_PIN, GPIO.HIGH)  # Assuming HIGH triggers relay OFF
    print("Fan is OFF")

# Function to turn pump on
def pump_on():
    GPIO.output(PUMP_PIN, GPIO.LOW)  # Assuming LOW triggers relay ON
    print("Pump is ON")

# Function to turn pump off
def pump_off():
    GPIO.output(PUMP_PIN, GPIO.HIGH)  # Assuming HIGH triggers relay OFF
    print("Pump is OFF")

# Main code
try:
    # Turn on fan and pump for 5 seconds each, with delays in between
    fan_on()
    time.sleep(5)
    fan_off()
    time.sleep(2)
    
    pump_on()
    time.sleep(5)
    pump_off()
    time.sleep(2)

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
