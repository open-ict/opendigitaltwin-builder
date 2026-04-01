import json
import time
import paho.mqtt.client as mqtt
from app.core.config import settings

def on_connect(client, userdata, flags, rc):
    print("MQTT connected:", rc)
    client.subscribe(settings.MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print("ingested:", payload)
    except Exception as e:
        print("MQTT error:", e)

while True:
    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(settings.MQTT_BROKER, settings.MQTT_PORT, 60)
        client.loop_forever()
    except Exception as e:
        print("Reconnect after error:", e)
        time.sleep(5)
