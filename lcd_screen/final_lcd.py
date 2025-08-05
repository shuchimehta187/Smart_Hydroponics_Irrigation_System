import time
import Adafruit_CharLCD as LCD

# Raspberry Pi pin setup
lcd_rs = 21  # Register Select pin
lcd_en = 20  # Enable pin
lcd_d4 = 16  # Data pin 4
lcd_d5 = 12  # Data pin 5
lcd_d6 = 1   # Data pin 6
lcd_d7 = 25  # Data pin 7
lcd_backlight = 2  # Backlight pin

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD using the pins defined
lcd = LCD.Adafruit_CharLCD(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
    lcd_columns, lcd_rows, lcd_backlight
)

# Display initial message
lcd.message('Mechatronics\nLab!')
time.sleep(5)  # Wait 5 seconds
lcd.clear()

# Get user input
text = input("Type something to be displayed: ")
lcd.message(text + "\nHow Are You")
time.sleep(10)  # Wait 10 seconds
lcd.clear()

# Display farewell message
lcd.message('Thanks\nMechatronics')
time.sleep(5)  # Wait 5 seconds
lcd.clear()
