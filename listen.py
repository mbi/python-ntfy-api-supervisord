import json

import requests

print("Subscribing...")
resp = requests.get("http://localhost:9999/my-topic/json", stream=True)
for line in resp.iter_lines():
    if line:
        payload = json.loads(line.decode())
        if payload.get("event") == "message":
            print(json.loads(payload.get("message")))
        else:
            print(payload)

print("Exiting...")
