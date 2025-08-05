import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import random  # Using random for sample data, replace with actual sensor read code

# AWS IoT Core connection parameters
clientID = "RaspberryPiClient"  # Unique client ID for the sensor
endpoint = "a2odkdimk1y8d4-ats.iot.ap-south-1.amazonaws.com"  # Replace with your IoT Core endpoint
certificatePath = "/home/pi/aws_keys_soil/cd1847cb9f4a8f19e02e8cda8e307bd6771cb939002a0ec18bf24cb5849b450c-certificate.pem.crt"     # Path to your device certificate
privateKeyPath = "/home/pi/aws_keys_soil/cd1847cb9f4a8f19e02e8cda8e307bd6771cb939002a0ec18bf24cb5849b450c-private.pem.key"          # Path to your device private key
rootCAPath = "/home/pi/aws_keys_soil/AmazonRootCA1.pem"            # Path to your root CA certificate

# Initialize and configure the AWS IoT MQTT client
client = AWSIoTMQTTClient(clientID)
client.configureEndpoint(endpoint, 8883)
client.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# Optional configurations for client
client.configureOfflinePublishQueueing(-1)  # Infinite offline publish queueing
client.configureDrainingFrequency(2)  # Draining: 2 Hz
client.configureConnectDisconnectTimeout(10)  # 10 sec
client.configureMQTTOperationTimeout(5)  # 5 sec

# Soil moisture sensor read function (replace with actual sensor read code)
def read_soil_moisture():
    # Replace this with the code to read data from the actual sensor
    # Example: using random values to simulate soil moisture readings
    return random.randint(300, 800)  # Example moisture range, adjust as needed

# Connect to AWS IoT Core
client.connect()

# Define the MQTT topic
topic = "sensors/soilMoisture"  # Define a topic for the sensor data

# Publish data in a loop
try:
    while True:
        # Read data from the soil moisture sensor
        moisture_level = read_soil_moisture()

        # Create a message payload
        payload = {
            "sensorID": clientID,
            "moistureLevel": moisture_level,
            "timestamp": int(time.time())
        }

        # Convert the payload to JSON and publish it to the topic
        client.publish(topic, json.dumps(payload), 1)
        print(f"Published: {payload} to topic: {topic}")

        # Wait before sending the next data
        time.sleep(10)  # Adjust the interval as needed

except KeyboardInterrupt:
    print("Stopped by user")

# Disconnect from AWS IoT Core
client.disconnect()
