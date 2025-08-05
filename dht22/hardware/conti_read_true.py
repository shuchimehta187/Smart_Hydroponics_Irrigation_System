from pigpio_dht import DHT11, DHT22
from time import sleep

gpio = 17 # BCM Numbering

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
        #else:
            #print('Failed to read data. Try again!')

        # Wait for a few seconds before taking the next reading
        sleep(3)
except KeyboardInterrupt:
    print("Measurement stopped by user")
