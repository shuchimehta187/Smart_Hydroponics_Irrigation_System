import pigpio
from time import sleep

# Initialize pigpio
pi = pigpio.pi()

# GPIO pin connected to the DHT22
DHT_PIN = 4

def read_dht22():
    # Read data from the sensor
    data = pi.read_dht22(DHT_PIN)

    # Check if data read was successful
    if data[0] == pigpio.DHT_GOOD:
        humidity = data[1] / 1000.0  # Humidity in percentage
        temperature = data[2] / 1000.0  # Temperature in Celsius
        print(f'Temperature: {temperature:.2f}C, Humidity: {humidity:.2f}%')
    else:
        print('Failed to get reading. Try again!')

while True:
    read_dht22()
    sleep(2)

# When done, cleanup
pi.stop()
