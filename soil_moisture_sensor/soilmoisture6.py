import RPi.GPIO as GPIO
import time
#from gpiozero import MCP3008
sensor_SOIL=27
#buzzer=38
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_SOIL, GPIO.IN)
#GPIO.setup(buzzer, GPIO.OUT)
#GPIO.output(buzzer, False)
#adc=MCP3008(channel=0)
print("SOIL Sensor Ready")
print()
start_time=time.time()
try:
    while True:
        #sensor_value=adc.value
        if GPIO.input(sensor_SOIL):
            #GPIO.output(buzzer, False)
            print("SOIL IS NOT DETECTED - Sensor value: 0")
            while GPIO.input(sensor_SOIL):
                time.sleep(0.2)
        else:
            end_time=time.time()
            #GPIO.output(buzzer, True)
            print("SOIL sensor is detected - Sensor value: 1 at time {:.2f} s".format(end_time-start_time))
except KeyboardInterrupt:
    GPIO.cleanup()
