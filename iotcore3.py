import RPi.GPIO as GPIO
import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# AWS IoT Core connection parameters
clientID = "RaspberryPiClient"  
endpoint = "a2odkdimk1y8d4-ats.iot.ap-south-1.amazonaws.com"  # Replace with your IoT Core endpoint
certificatePath = "/home/pi/aws_keys_fan/8a33162087cfca13468f51a769712a8664cd0fdb8fb10427554ee2011a50c836-certificate.pem.crt"     # Path to your device certificate
privateKeyPath = "/home/pi/aws_keys_fan/8a33162087cfca13468f51a769712a8664cd0fdb8fb10427554ee2011a50c836-private.pem.key"          # Path to your device private key
rootCAPath = "/home/pi/aws_keys_fan/AmazonRootCA1.pem"            # Path to your root CA certificate

# GPIO setup for fan relay
fan_relay_pin = 17  # GPIO pin connected to the fan relay control pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_relay_pin, GPIO.OUT)

# Initialize the relay to an OFF state (check if relay is active LOW or HIGH)
GPIO.output(fan_relay_pin, GPIO.HIGH)  # Assuming HIGH is off for active LOW relay

# Initialize AWS IoT MQTT client
client = AWSIoTMQTTClient(clientID)
client.configureEndpoint(endpoint, 8883)
client.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

client.configureOfflinePublishQueueing(-1)
client.configureDrainingFrequency(2)
client.configureConnectDisconnectTimeout(10)
client.configureMQTTOperationTimeout(5)

# Callback function for fan control
def fan_callback(client, userdata, message):
    payload = json.loads(message.payload)
    if payload["state"] == "ON":
        GPIO.output(fan_relay_pin, GPIO.LOW)  # Turn on the relay (assuming active LOW)
        print("Fan turned ON")
    else:
        GPIO.output(fan_relay_pin, GPIO.HIGH)  # Turn off the relay
        print("Fan turned OFF")

# Connect to AWS IoT Core and subscribe to fan topic
client.connect()
client.subscribe("actuators/fan", 1, fan_callback)

try:
    print("Listening for fan commands...")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    GPIO.output(fan_relay_pin, GPIO.HIGH)  # Turn off the relay on exit
    GPIO.cleanup()
    client.disconnect()
