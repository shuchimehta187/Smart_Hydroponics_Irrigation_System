import paho.mqtt.client as mqtt
import pigpio
from pigpio_dht import DHT22
import ssl
import time
import json

# AWS IoT Core endpoint (replace with your endpoint)
AWS_ENDPOINT = "a2odkdimk1y8d4-ats.iot.ap-south-1.amazonaws.com"
AWS_PORT = 8883

# AWS IoT Core certificate paths
CA_PATH = "/home/pi/aws_keys_dht22/AmazonRootCA1.pem"
CERT_PATH = "/home/pi/aws_keys_dht22/fe99c465672cf1dc3e560ca286a00c37929d0b2e8e0083dca5c9825712dd4129-certificate.pem.crt"
KEY_PATH = "/home/pi/aws_keys_dht22/fe99c465672cf1dc3e560ca286a00c37929d0b2e8e0083dca5c9825712dd4129-public.pem.key"

# DHT22 sensor setup (GPIO pin number)
DHT_PIN =17  # Replace with the GPIO pin you're using for the DHT22

# Initialize pigpio
pi = pigpio.pi()
pi.set_pull_up_down(DHT_PIN, pigpio.PUD_UP)
SENSOR=DHT22(pi, DHT_PIN)

# Check if pigpio connection is successful
if not pi.connected:
    print("Failed to connect to pigpio daemon!")
    exit()

# Try to initialize the sensor and catch any errors
try:
    SENSOR = DHT22(pi, DHT_PIN)
except Exception as e:
    print(f"Error initializing the sensor: {e}")
    exit()

# MQTT topic to publish sensor data
MQTT_TOPIC = "sensors/dht22/gpio17"

# Callback for connection status
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to AWS IoT Core")
    else:
        print(f"Failed to connect with code {rc}")

# Callback when a message is published
def on_publish(client, userdata, mid):
    print("Message published")

# Create the MQTT client
client = mqtt.Client()

# Configure the client for TLS
client.tls_set(ca_certs=CA_PATH, certfile=CERT_PATH, keyfile=KEY_PATH, tls_version=ssl.PROTOCOL_TLSv1_2)

# Set callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to AWS IoT Core
client.connect(AWS_ENDPOINT, AWS_PORT, keepalive=60)

# Start the network loop
client.loop_start()

# Publish sensor data in a loop
while True:
    # Read data from DHT22 sensor
    result = SENSOR.read()

    if result['valid']:
        temperature = result['temp_c']
        humidity = result['humidity']

        # Create payload
        payload = json.dumps({
            "temperature": temperature,
            "humidity": humidity
        })

        # Publish the payload to the MQTT topic
        client.publish(MQTT_TOPIC, payload)

        print(f"Published: {payload}")
    else:
        print("Failed to get reading from the sensor")

    # Wait 10 seconds before sending the next reading
    time.sleep(10)
