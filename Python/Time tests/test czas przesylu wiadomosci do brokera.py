import paho.mqtt.client as mqtt
from timeit import default_timer as timer
from datetime import timedelta
import time
end = 0

def on_connect(client, userdata, flags, rc):
    print(f"Connected to the broker with result code {rc}")
    if rc == 0:
        client.publish(topic = "Test-1/STATUS/CONNECTION", payload = "ONLINE", qos = 0, retain = False)   

def on_publish(client, userdata, mid):
    global end
    end = timer()
    print(timedelta(seconds=end-start))
    print('lol')
      
def on_message(client, userdata, msg):
    print(f"topic: {msg.topic}, payload: {msg.payload.decode('utf-8')}")


mqttHost = '192.168.99.90'
mqttPort = 1883

client = mqtt.Client(client_id="pcClient")

client.on_connect = on_connect

client.on_publish = on_publish
client.on_message = on_message

# client.will_set(topic = "ORZEL_PC/STATUS/CONNECTION", payload = "OFFLINE", retain = True)
start = timer()
client.connect(host = mqttHost, port = mqttPort, keepalive = 10)

client.loop_forever()
