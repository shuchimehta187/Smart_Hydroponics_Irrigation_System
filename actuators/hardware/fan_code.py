from pigpio_dht import DHT11, DHT22
from time import sleep, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
FAN_PIN = 17 # BCM Numbering
GPIO.setup(FAN_PIN, GPIO.OUT)
FAN_THRESHOLD=-30.0
fan_on=False
overheat_start=None
gpio=7

# Create a sensor object for DHT11 sensor
sensor = DHT22(gpio)
# Or create a sensor object for DHT22 sensor
# sensor = DHT22(gpio)

try:
    while True:
        # Read sensor data
        result = sensor.read()
        
        # Check if reading was successful
        #if result.is_valid():
            # Display temperature and humidity
        #print(f'Temperature: {result.temp_c:.2f}°C, Humidity: {result.humidity:.2f}%')
        result['temp_c']=max(result['temp_c']-720,0)
        result['temp_f']=9*result['temp_c']/5+32
        if result['valid']==True:
                print(result)
                temperature=result['temp_c']
                if temperature>FAN_THRESHOLD:
                        if not fan_on:
                                if overheat_start is None:
                                        overheat_start=time()
                                elif time()-overheat_start>=5:
                                        GPIO.output(FAN_PIN, GPIO.LOW)
                                        fan_on=True
                                        print("fan turned on")
                                else:
                                        overheat_start=None
                        else:
                                if fan_on:
                                        GPIO.output(FAN_PIN, GPIO.HIGH)
                                        fan_on=False
                                        print("Fan turned off")
                                        
        #else:
            #print('Failed to read data. Try again!')

        # Wait for a few seconds before taking the next reading
        sleep(3)
except KeyboardInterrupt:
    print("Measurement stopped by user")
finally:
        GPIO.output(FAN_PIN, GPIO.HIGH)
        GPIO.cleanup()
