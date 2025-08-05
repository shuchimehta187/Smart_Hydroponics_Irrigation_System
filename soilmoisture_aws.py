import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import RPi.GPIO as GPIO

# Soil moisture sensor GPIO pin
sensor_SOIL = 27

# AWS IoT Core connection parameters
clientID = "RaspberryPiClient"
endpoint = "a2odkdimk1y8d4-ats.iot.ap-south-1.amazonaws.com"  # Replace with your IoT Core endpoint
certificatePath = "/home/pi/aws_keys_soil/cd1847cb9f4a8f19e02e8cda8e307bd6771cb939002a0ec18bf24cb5849b450c-certificate.pem.crt"     # Path to your device certificate
privateKeyPath = "/home/pi/aws_keys_soil/cd1847cb9f4a8f19e02e8cda8e307bd6771cb939002a0ec18bf24cb5849b450c-private.pem.key"          # Path to your device private key
rootCAPath = "/home/pi/aws_keys_soil/AmazonRootCA1.pem"            # Path to your root CA certificate

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_SOIL, GPIO.IN)

# Initialize and configure the AWS IoT MQTT client
client = AWSIoTMQTTClient(clientID)
client.configureEndpoint(endpoint, 8883)
client.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# MQTT client configuration
client.configureOfflinePublishQueueing(-1)  # Infinite offline publish queueing
client.configureDrainingFrequency(2)  # Draining frequency: 2 Hz
client.configureConnectDisconnectTimeout(10)  # Connection timeout: 10 seconds
client.configureMQTTOperationTimeout(5)  # Operation timeout: 5 seconds

# Connect to AWS IoT Core
client.connect()

# Define the MQTT topic
topic = "sensors/soilMoisture"

# Read soil moisture and publish to AWS IoT Core
try:
    print("SOIL Sensor Ready")
    while True:
        # Read soil moisture sensor status
        soil_detected = not GPIO.input(sensor_SOIL)  # Assuming LOW indicates soil presence
        
        # Create a message payload
        payload = {
            "sensorID": clientID,
            "moistureDetected": soil_detected,  # True if soil is detected, False otherwise
            "timestamp": int(time.time())
        }
        
        # Publish the payload to AWS IoT Core
        client.publish(topic, json.dumps(payload), 1)
        print(f"Published: {payload} to topic: {topic}")
        
        # Wait before sending the next data
        time.sleep(4)  # Adjust the interval as needed

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    # Clean up GPIO and disconnect from AWS IoT Core
    GPIO.cleanup()
    client.disconnect()
