import json
import time
import random
import paho.mqtt.publish as publish

while True:
    payload = {
        "tenant_id": 1,
        "asset_uid": "hive-001",
        "temperature": round(random.uniform(34.0, 40.5), 2),
        "humidity": round(random.uniform(48.0, 68.0), 2),
        "weight": round(random.uniform(8.0, 22.0), 2),
        "sound_index": round(random.uniform(0.2, 1.0), 2),
    }
    publish.single("opendt/telemetry", json.dumps(payload), hostname="localhost")
    print("published", payload)
    time.sleep(5)
