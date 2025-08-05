display=lcddriver.lcd()
try:
    while True:
        print("Writing to display")
        display.lcd_display_string("Greetings Human!",1)
        display.lcd_display_string("Demo Pi Guy Code", 2)
        time.sleep(2)
        display.lcd_display_string("I am a display!",1)
        time.sleep(2)
        display.lcd_clear()
        time.sleep(2)
except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
    