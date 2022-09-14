import paho.mqtt.client as mqtt
from timeit import default_timer as timer
from datetime import timedelta
start = 0
end = 0
mqttText = "Loremipsumdolorsitamet,consekjksdhlfshdlfusdfuuuuuuuuuuuuuuuuudhffffffffdufhufdhhuffdhudufhdfuhdfhuhskdfhsdifhksfdh9"

mqttTopicPC = "PC/EVENTS"
mqttTopicPLC = "PLC/EVENTS"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to the broker with result code {rc}")
    if rc == 0:
        client.subscribe(mqttTopicPLC, qos = 1)
        client.publish(topic = mqttTopicPC, payload = mqttText, qos = 1, retain = False)

def on_publish(client, userdata, mid):
    global start
    start = timer()
    print("timer zaczyna odliczanie")

def on_message(client, userdata, msg):
    if msg.topic == mqttTopicPLC and msg.payload.decode('utf-8') == "test":
        global end
        end = timer()
        print(timedelta(seconds=end-start))
    
mqttHost = '192.168.99.90'
mqttPort = 1883

client = mqtt.Client(client_id="pcClient")

client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

client.connect(host = mqttHost, port = mqttPort, keepalive = 10)

print('before')
client.loop_forever()
print('after')

