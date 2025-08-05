import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

# Define LCD size (16x2)
lcd_columns = 16
lcd_rows = 2

# Define pin configuration
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d4 = digitalio.DigitalInOut(board.D13)
lcd_d5 = digitalio.DigitalInOut(board.D06)
lcd_d6 = digitalio.DigitalInOut(board.D05)
lcd_d7 = digitalio.DigitalInOut(board.D11)
lcd_backlight = digitalio.DigitalInOut(board.D04)

# Initialize the LCD class
lcd = character_lcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
    lcd_columns, lcd_rows, lcd_backlight
)

# Print a message to the LCD
lcd.message = "Hello, World!\nLCD with RPi"
