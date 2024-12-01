import sqlite3
import paho.mqtt.client as mqtt


BROKER = 'localhost'
TOPIC = 'sensors/temperature'

def insert_into_database(temperature):
    print("Writing to database")
    conn = sqlite3.connect('../../database/hometemp.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO temperature_readings (temperature)
    VALUES (?)
    ''', (temperature,))
    conn.commit()
    conn.close()

# Define MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode())
    print("Received!")
    insert_into_database(temperature)

# Set up MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER)
client.loop_forever()
