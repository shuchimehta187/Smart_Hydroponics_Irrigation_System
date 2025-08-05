import paho.mqtt.client as mqtt
import pigpio
from pigpio_dht import DHT22
import ssl
import time
import json

# AWS IoT Core endpoint (replace with your endpoint)
AWS_ENDPOINT = "your-aws-iot-endpoint-ats.iot.ap-south-1.amazonaws.com"
AWS_PORT = 8883

# AWS IoT Core certificate paths
CA_PATH = "/path/to/AmazonRootCA1.pem"
CERT_PATH = "/path/to/xxx-certificate.pem.crt"
KEY_PATH = "/path/to/xxx-private.pem.key"

# DHT22 sensor setup (GPIO pin number)
DHT_PIN = 17  # Replace with the GPIO pin you're using for the DHT22
pi = pigpio.pi()  # Initialize pigpio
SENSOR = DHT22(pi, DHT_PIN)  # Correct class instantiation

# MQTT topic to publish sensor data, reflecting GPIO pin
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
