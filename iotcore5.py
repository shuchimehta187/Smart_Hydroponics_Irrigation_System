import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# AWS IoT Core connection parameters
clientID = "RaspberryPiClient"  
endpoint = "a2odkdimk1y8d4-ats.iot.ap-south-1.amazonaws.com"  # Replace with your IoT Core endpoint
certificatePath = "/home/pi/aws_keys_pump/587466cc90c04479c82194b791e3f47b4023a65d4495b1ef5b83c9a4b92a8de2-certificate.pem.crt"     # Path to your device certificate
privateKeyPath = "/home/pi/aws_keys_pump/587466cc90c04479c82194b791e3f47b4023a65d4495b1ef5b83c9a4b92a8de2-private.pem.key"          # Path to your device private key
rootCAPath = "/home/pi/aws_keys_pump/AmazonRootCA1.pem"            # Path to your root CA certificate

# Initialize AWS IoT MQTT client
client = AWSIoTMQTTClient(clientID)
client.configureEndpoint(endpoint, 8883)
client.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

client.configureOfflinePublishQueueing(-1)
client.configureDrainingFrequency(2)
client.configureConnectDisconnectTimeout(10)
client.configureMQTTOperationTimeout(5)

# Callback function for pump control (simulation)
def pump_callback(client, userdata, message):
    payload = json.loads(message.payload)
    print("Received command for pump:")
    print(f"State: {payload['state']}")  # Simulate received state (ON/OFF)

# Connect to AWS IoT Core and subscribe to the pump topic
client.connect()
client.subscribe("actuators/pump", 1, pump_callback)

try:
    print("Listening for pump commands (simulation mode)...")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    client.disconnect()
