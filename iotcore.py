from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json

# Initialize your client instance
client = AWSIoTMQTTClient("RaspberryPiClient")
client.configureEndpoint("a2odkdimk1y8d4-ats.iot.ap-south-1.amazonaws.com", 8883)
client.configureCredentials(
    "/home/pi/aws_keys_dht22/AmazonRootCA1.pem",      # Path to Root CA certificate
    "/home/pi/aws_keys_dht22/fe99c465672cf1dc3e560ca286a00c37929d0b2e8e0083dca5c9825712dd4129-private.pem.key",        # Path to private key
    "/home/pi/aws_keys_dht22/fe99c465672cf1dc3e560ca286a00c37929d0b2e8e0083dca5c9825712dd4129-certificate.pem.crt"     # Path to device certificate
)

# MQTT connection configurations
client.configureOfflinePublishQueueing(-1)  # Infinite offline publishing
client.configureDrainingFrequency(2)  # Draining frequency in Hz
client.configureConnectDisconnectTimeout(10)  # 10 seconds
client.configureMQTTOperationTimeout(5)  # 5 seconds

# Connect to AWS IoT Core
client.connect()
print("Connected to AWS IoT Core")

# Define a function to publish sensor data
def publish_sensor_data():
    while True:
        # Example of dummy sensor data
        sensor_data = {
            "temperature": 23.5,
            "humidity": 56.2
        }
        
        # Publish data as JSON to the topic
        client.publish("raspberrypi/sensors", json.dumps(sensor_data), 1)
        print("Data published:", sensor_data)
        
        time.sleep(5)  # Delay between data sends (adjust as needed)

# Start publishing
publish_sensor_data()
