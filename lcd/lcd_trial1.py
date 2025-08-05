import RPi.GPIO as GPIO
from time import sleep

# GPIO Pin Configuration
RS = 7
E = 8
D0 = 14
D1 = 15
D2 = 18
D3 = 23
D4 = 24
D5 = 25
D6 = 20
D7 = 21

# GPIO Setup
#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup([RS, E], GPIO.OUT)
GPIO.setup([D0, D1, D2, D3, D4, D5, D6, D7], GPIO.OUT)

def lcd_send_byte(byte, mode):
    GPIO.output(RS, mode)
    GPIO.output(E, True)
    
    GPIO.output(D0, byte & 0x01)
    GPIO.output(D1, byte & 0x02)
    GPIO.output(D2, byte & 0x04)
    GPIO.output(D3, byte & 0x08)
    GPIO.output(D4, byte & 0x10)
    GPIO.output(D5, byte & 0x20)
    GPIO.output(D6, byte & 0x40)
    GPIO.output(D7, byte & 0x80)
    
    GPIO.output(E, False)
    sleep(0.001)
    GPIO.output(E, True)
    sleep(0.001)
    GPIO.output(E, False)
    sleep(0.002)

def lcd_initialize():
    lcd_send_byte(0x38, False) # Function set: 8-bit mode
    lcd_send_byte(0x0C, False) # Display ON, Cursor OFF
    lcd_send_byte(0x06, False) # Entry mode set: Increment cursor
    lcd_send_byte(0x01, False) # Clear display
    sleep(0.002)

def lcd_print_message(message):
    for char in message:
        lcd_send_byte(ord(char), True)

try:
    lcd_initialize()
    lcd_print_message("Hello, World!")
finally:
    GPIO.cleanup()
