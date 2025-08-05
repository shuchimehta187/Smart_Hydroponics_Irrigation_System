import time
import Adafruit_CharLCD as LCD
lcd_rs=21
lcd_en=20
lcd_d4=16
lcd_d5=12
lcd_d6=1
lcd_d7=25
lcd_backlight=2
lcd_columns=16
lcd_rows=2
lcd=LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
lcd.message("Hello")
time.sleep(5.0)
lcd.clear()
text=raw_input("Type something to be displayed")
lcd.message(text="How are you?")
time.sleep(10.0)
lcd.clear()
lcd.message("Thanks!")
time.sleep(5.0)
