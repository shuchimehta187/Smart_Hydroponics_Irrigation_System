import smbus
import time

# Define I2C device address (use 'i2cdetect -y 1' to find your address)
LCD_ADDR = 0x27

# Define some device constants
LCD_WIDTH = 16   # Maximum characters per line

# LCD commands
LCD_CLEAR = 0x01  # Clear display
LCD_RETURN_HOME = 0x02  # Return to home position

# LCD entry mode
LCD_ENTRY_MODE = 0x06

# LCD display control
LCD_DISPLAY_CONTROL = 0x08 | 0x04  # Display on, cursor off, blink off

# Function set
LCD_FUNCTION_SET = 0x20 | 0x08  # 4-bit mode, 2 lines, 5x8 font

# Define GPIO to LCD mapping (adjust these as per your wiring)
LCD_BACKLIGHT = 0x08  # On
LCD_NOBACKLIGHT = 0x00  # Off

En = 0b00000100  # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 1

# Open I2C interface
bus = smbus.SMBus(1)  # Use '1' for Raspberry Pi version 2 or 3 with 1GB RAM or more (2GB)

def lcd_init():
    # Initialize display
    lcd_byte(0x03, False)
    lcd_byte(0x03, False)
    lcd_byte(0x03, False)
    lcd_byte(0x02, False)
    lcd_byte(LCD_FUNCTION_SET, False)
    lcd_byte(LCD_CLEAR, False)
    lcd_byte(LCD_ENTRY_MODE, False)
    lcd_byte(LCD_DISPLAY_CONTROL, False)

def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command

    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    # High bits
    bus.write_byte(LCD_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    # Low bits
    bus.write_byte(LCD_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    # Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(LCD_ADDR, (bits | En))
    time.sleep(E_PULSE)
    bus.write_byte(LCD_ADDR, (bits & ~En))
    time.sleep(E_DELAY)

def lcd_string(message, line):
    # Send string to display
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, False)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), True)

if __name__ == '__main__':
    try:
        lcd_init()
        lcd_string("Hello", 0x80)  # Display "Hello" on first line

        while True:
            pass  # Your main loop can go here

    except KeyboardInterrupt:
        lcd_byte(LCD_CLEAR, False)
        lcd_string("Goodbye!", 0x80)

    finally:
        bus.close()
