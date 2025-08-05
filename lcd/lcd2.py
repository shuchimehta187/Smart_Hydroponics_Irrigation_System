from RPLCD import NoBackend
from RPLCD.i2c import CharLCDI2C
import time

# Set up the LCD (change the address if needed)
lcd = CharLCDI2C('PCF8574', 0x27)

# Clear the LCD
lcd.clear()

# Display text
lcd.write_string('Hello, World!')

# Wait for 5 seconds
time.sleep(5)

# Clear the display
lcd.clear()
