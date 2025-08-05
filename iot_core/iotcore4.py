import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# AWS IoT Core connection parameters
clientID = "RaspberryPiClient"  
endpoint = "a2odkdimk1y8d4-ats.iot.ap-south-1.amazonaws.com"  # Replace with your IoT Core endpoint
certificatePath = "/home/pi/aws_keys_fan/8a33162087cfca13468f51a769712a8664cd0fdb8fb10427554ee2011a50c836-certificate.pem.crt"     # Path to your device certificate
privateKeyPath = "/home/pi/aws_keys_fan/8a33162087cfca13468f51a769712a8664cd0fdb8fb10427554ee2011a50c836-private.pem.key"          # Path to your device private key
rootCAPath = "/home/pi/aws_keys_fan/AmazonRootCA1.pem"            # Path to your root CA certificate

# Initialize AWS IoT MQTT client
client = AWSIoTMQTTClient(clientID)
client.configureEndpoint(endpoint, 8883)
client.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

client.configureOfflinePublishQueueing(-1)
client.configureDrainingFrequency(2)
client.configureConnectDisconnectTimeout(10)
client.configureMQTTOperationTimeout(5)

# Callback function for fan control (simulation)
def fan_callback(client, userdata, message):
    payload = json.loads(message.payload)
    print("Received command for fan:")
    print(f"State: {payload['state']}")  # Simulate received state (ON/OFF)

# Connect to AWS IoT Core and subscribe to the fan topic
client.connect()
client.subscribe("actuators/fan", 1, fan_callback)

try:
    print("Listening for fan commands (simulation mode)...")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    client.disconnect()
