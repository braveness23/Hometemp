"""module that creates a mmqt topic and publishes to it"""
import random
import time
import paho.mqtt.client as mqtt

BROKER = 'localhost'
TOPIC = 'sensors/temperature'

def publish_temperature():
    """publish temperature"""
    client = mqtt.Client()
    client.connect(BROKER)

    while True:
        temperature = round(random.uniform(15.0, 30.0), 2)  # Simulate temperature reading
        client.publish(TOPIC, temperature)
        print("Published: {temperature}")
        time.sleep(5)  # Publish every 5 seconds

publish_temperature()
