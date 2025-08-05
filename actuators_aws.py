import time
import json
import RPi.GPIO as GPIO
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# AWS IoT Core connection parameters
clientID = "RaspberryPiClient"
endpoint = "a2odkdimk1y8d4-ats.iot.ap-south-1.amazonaws.com"  # Replace with your IoT Core endpoint
certificatePath = "/home/pi/aws_keys_pump/587466cc90c04479c82194b791e3f47b4023a65d4495b1ef5b83c9a4b92a8de2-certificate.pem.crt"     # Path to your device certificate
privateKeyPath = "/home/pi/aws_keys_pump/587466cc90c04479c82194b791e3f47b4023a65d4495b1ef5b83c9a4b92a8de2-private.pem.key"          # Path to your device private key
rootCAPath = "/home/pi/aws_keys_pump/AmazonRootCA1.pem"            # Path to your root CA certificate

# GPIO setup for actuators
FAN_PIN = 17
PUMP_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.setup(PUMP_PIN, GPIO.OUT)

# Initialize AWS IoT MQTT client
client = AWSIoTMQTTClient(clientID)
client.configureEndpoint(endpoint, 8883)
client.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# MQTT client configuration for reconnection and timeouts
client.configureOfflinePublishQueueing(-1)  # Infinite offline publish queueing
client.configureDrainingFrequency(2)        # Draining frequency: 2 Hz
client.configureConnectDisconnectTimeout(10)  # Connection timeout: 10 seconds
client.configureMQTTOperationTimeout(5)       # Operation timeout: 5 seconds

# Callback function to control actuators based on message received
def on_message(client, userdata, message):
    data = json.loads(message.payload)
    print("Message received:", data)
    
    # Control fan
    if data.get("fan") == "on":
        GPIO.output(FAN_PIN, GPIO.LOW)  # Activate fan (LOW might turn on depending on relay setup)
        print("Fan turned ON")
    elif data.get("fan") == "off":
        GPIO.output(FAN_PIN, GPIO.HIGH)  # Deactivate fan
        print("Fan turned OFF")
    
    # Control pump
    if data.get("pump") == "on":
        GPIO.output(PUMP_PIN, GPIO.LOW)  # Activate pump
        print("Pump turned ON")
    elif data.get("pump") == "off":
        GPIO.output(PUMP_PIN, GPIO.HIGH)  # Deactivate pump
        print("Pump turned OFF")

# Connect to AWS IoT Core and subscribe to the relevant topic
client.connect()
client.subscribe("actuators/fan", 1, on_message)

try:
    print("Listening for actuator control commands...")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Process stopped by user")

finally:
    # Clean up GPIO on exit
    GPIO.cleanup()
    client.disconnect()
