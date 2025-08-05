import pigpio_dht
import pigpio
from pigpio_dht import DHT11, DHT22
import time

# Initialize pigpio and the DHT22 sensor
pi = pigpio.pi()
gpio=27
dht22 = DHT22(gpio)  # Use GPIO pin 4

# Read data from the sensor
while True:
    #dht22.trigger()
    result=dht22.read()
    '''humidity = dht22.humidity()
    temperature = dht22.temperature()
    
    if humidity is not None and temperature is not None:
        print(f"Temp={temperature:.1f}C  Humidity={humidity:.1f}%")
    else:
        print("Failed to retrieve data from humidity sensor")'''
    print(result)
    time.sleep(2)
