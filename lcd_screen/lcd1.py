import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping
lcd_rs = 21
lcd_en = 20
lcd_d4 = 16
lcd_d5 = 12
lcd_d6 = 1
lcd_d7 = 25
lcd_backlight = 2

# Define LCD parameters
lcd_columns = 16
lcd_rows = 2

# Define GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(lcd_rs, GPIO.OUT)
GPIO.setup(lcd_en, GPIO.OUT)
GPIO.setup(lcd_d4, GPIO.OUT)
GPIO.setup(lcd_d5, GPIO.OUT)
GPIO.setup(lcd_d6, GPIO.OUT)
GPIO.setup(lcd_d7, GPIO.OUT)
GPIO.setup(lcd_backlight, GPIO.OUT)

# Function to send a command to the LCD
def lcd_send_command(cmd):
    GPIO.output(lcd_rs, False)  # RS = 0 for command
    lcd_send_byte(cmd)
    time.sleep(0.001)

# Function to send data to the LCD
def lcd_send_data(data):
    GPIO.output(lcd_rs, True)  # RS = 1 for data
    lcd_send_byte(data)
    time.sleep(0.001)

# Function to send a byte to the LCD
def lcd_send_byte(bits):
    GPIO.output(lcd_d4, False)
    GPIO.output(lcd_d5, False)
    GPIO.output(lcd_d6, False)
    GPIO.output(lcd_d7, False)
    if bits & 0x10 == 0x10:
        GPIO.output(lcd_d4, True)
    if bits & 0x20 == 0x20:
        GPIO.output(lcd_d5, True)
    if bits & 0x40 == 0x40:
        GPIO.output(lcd_d6, True)
    if bits & 0x80 == 0x80:
        GPIO.output(lcd_d7, True)
    lcd_toggle_enable()
    
    GPIO.output(lcd_d4, False)
    GPIO.output(lcd_d5, False)
    GPIO.output(lcd_d6, False)
    GPIO.output(lcd_d7, False)
    if bits & 0x01 == 0x01:
        GPIO.output(lcd_d4, True)
    if bits & 0x02 == 0x02:
        GPIO.output(lcd_d5, True)
    if bits & 0x04 == 0x04:
        GPIO.output(lcd_d6, True)
    if bits & 0x08 == 0x08:
        GPIO.output(lcd_d7, True)
    lcd_toggle_enable()

# Function to toggle the enable pin
def lcd_toggle_enable():
    time.sleep(0.0005)
    GPIO.output(lcd_en, True)
    time.sleep(0.0005)
    GPIO.output(lcd_en, False)
    time.sleep(0.0005)

# Function to initialize the LCD
def lcd_init():
    lcd_send_command(0x33)  # 110011 Initialize
    lcd_send_command(0x32)  # 110010 Initialize
    lcd_send_command(0x28)  # 101000 Data length, number of lines, font size
    lcd_send_command(0x0C)  # 001100 Display on, cursor off, blink off
    lcd_send_command(0x06)  # 000110 Increment cursor
    lcd_send_command(0x01)  # 000001 Clear display

# Function to display a message on the LCD
def lcd_message(message):
    for char in message:
        lcd_send_data(ord(char))

# Initialize the LCD
lcd_init()

# Display a message on the LCD
lcd_message('Mechatronics\nLab!')
time.sleep(5.0)
GPIO.output(lcd_backlight, False)  # Turn off backlight

# Clear the LCD
lcd_send_command(0x01)

# Ask for user input
text = input("Type Something to be displayed: ")
GPIO.output(lcd_backlight, True)  # Turn on backlight
lcd_message(text + "\nHow Are You")

# Wait 10 seconds
time.sleep(10.0)

# Clear the LCD and display the final message
lcd_send_command(0x01)
lcd_message('Thanks\nMechatronics')
time.sleep(5.0)

# Clean up the GPIO
GPIO.cleanup()
