import pigpio_dht
import pigpio
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time

# Initialize pigpio and the DHT22 sensor
pi = pigpio.pi()
gpio = 22
dht22 = pigpio_dht.DHT22(gpio)

# AWS IoT Core connection parameters
clientID = "RaspberryPiClient"
endpoint = "a2odkdimk1y8d4-ats.iot.ap-south-1.amazonaws.com"  # Replace with your IoT Core endpoint
certificatePath = "/home/pi/aws_keys_dht22/fe99c465672cf1dc3e560ca286a00c37929d0b2e8e0083dca5c9825712dd4129-certificate.pem.crt"
privateKeyPath = "/home/pi/aws_keys_dht22/fe99c465672cf1dc3e560ca286a00c37929d0b2e8e0083dca5c9825712dd4129-private.pem.key"
rootCAPath = "/home/pi/aws_keys_dht22/AmazonRootCA1.pem"

# Initialize and configure the AWS IoT MQTT client
client = AWSIoTMQTTClient(clientID)
client.configureEndpoint(endpoint, 8883)
client.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# Optional configurations for client
client.configureOfflinePublishQueueing(-1)  # Infinite offline publish queueing
client.configureDrainingFrequency(2)  # Draining: 2 Hz
client.configureConnectDisconnectTimeout(10)  # 10 sec
client.configureMQTTOperationTimeout(5)  # 5 sec

# Connect to AWS IoT Core
client.connect()
print("Connected to AWS IoT Core")

# Define the MQTT topic for DHT22 sensor data
topic = "sensors/dht22"

# Function to publish sensor data
def publish_sensor_data():
    while True:
        # Trigger a reading from the DHT22 sensor
        result = dht22.read()
        
        # Check if the reading is valid
        if result["valid"]:
            temperature = result["temp_c"]
            humidity = result["humidity"]

            # Create a payload for the MQTT message
            payload = {
                "sensorID": clientID,
                "temperature": temperature,
                "humidity": humidity,
                "timestamp": int(time.time())
            }
            
            # Publish the data to AWS IoT Core
            client.publish(topic, json.dumps(payload), 1)
            print(f"Published: {payload} to topic: {topic}")
        else:
            print("Failed to retrieve data from DHT22 sensor")

        # Delay between data sends (adjust as needed)
        time.sleep(5)

# Start publishing sensor data
try:
    publish_sensor_data()
except KeyboardInterrupt:
    print("Stopped by user")
finally:
    # Disconnect from AWS IoT Core
    client.disconnect()
    print("Disconnected from AWS IoT Core")
