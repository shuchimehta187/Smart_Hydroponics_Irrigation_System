import smbus
import time

# I2C device address (use 'i2cdetect -y 1' to find your address)
I2C_ADDR = 0x27  # Change this to your I2C address
LCD_WIDTH = 16   # Maximum characters per line

# LCD RAM address for lines
LCD_LINE_1 = 0x80  # 1st line
LCD_LINE_2 = 0xC0  # 2nd line

# LCD commands
LCD_CLEAR = 0x01  # Clear display
LCD_HOME = 0x02  # Return home
LCD_ENTRY_MODE_SET = 0x04  # Set entry mode
LCD_DISPLAY_CONTROL = 0x08  # Display control
LCD_FUNCTION_SET = 0x20  # Function set

LCD_ENTRY_LEFT = 0x02  # Entry left
LCD_ENTRY_SHIFT_INCREMENT = 0x01  # Shift increment
LCD_DISPLAY_ON = 0x04  # Display on
LCD_CURSOR_OFF = 0x00  # Cursor off
LCD_BLINK_OFF = 0x00  # Blink off
LCD_2LINE = 0x08  # 2 lines
LCD_5x8DOTS = 0x00  # 5x8 dots

LCD_BACKLIGHT = 0x08  # On
LCD_NOBACKLIGHT = 0x00  # Off

En = 0b00000100  # Enable bit
Rs = 0b00000001  # Register select bit

# Open I2C interface
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def lcd_init():
    lcd_byte(0x33, False)  # 110011 Initialize
    lcd_byte(0x32, False)  # 110010 Initialize
    lcd_byte(LCD_FUNCTION_SET | LCD_2LINE | LCD_5x8DOTS, False)
    lcd_byte(LCD_DISPLAY_CONTROL | LCD_DISPLAY_ON | LCD_CURSOR_OFF | LCD_BLINK_OFF, False)
    lcd_byte(LCD_CLEAR, False)
    lcd_byte(LCD_ENTRY_MODE_SET | LCD_ENTRY_LEFT | LCD_ENTRY_SHIFT_INCREMENT, False)
    time.sleep(0.2)

def lcd_byte(bits, mode):
    high_bits = mode | (bits & 0xF0) | LCD_BACKLIGHT
    low_bits = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    bus.write_byte(I2C_ADDR, high_bits)
    lcd_toggle_enable(high_bits)

    bus.write_byte(I2C_ADDR, low_bits)
    lcd_toggle_enable(low_bits)

def lcd_toggle_enable(bits):
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits | En))
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits & ~En))
    time.sleep(0.0005)

def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, False)
    for char in message:
        lcd_byte(ord(char), True)

if __name__ == '__main__':
    try:
        lcd_init()
        lcd_string("Hello", LCD_LINE_1)

        while True:
            lcd_string("Hello", LCD_LINE_1)
            time.sleep(10)

    except KeyboardInterrupt:
        lcd_byte(LCD_CLEAR, False)
        lcd_string("Goodbye!", LCD_LINE_1)
        bus.close()
