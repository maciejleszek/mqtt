import paho.mqtt.client as mqtt
import time
import lol

mqttServoCMD = "SERVO/CMD"
mqttServoConnection = "SERVO/CONNECTION"
napedConnected = False

def on_connect(client, userdata, flags, rc):
    print(f"Connected to the broker with result code {rc}")
    if rc == 0:
        client.subscribe(mqttServoConnection, qos = 0)

def on_publish(client, userdata, mid):
   pass

def on_message(client, userdata, msg):
    global napedConnected
    if msg.topic == mqttServoConnection and msg.payload.decode('utf-8') == "ONLINE":
        print("Napęd jest podłączony")
        napedConnected = True
    elif msg.topic == mqttServoConnection and msg.payload.decode('utf-8') == "OFFLINE":
        print("Napęd nie jest podłączony")
        napedConnected = False
       
mqttHost = '192.168.99.100'
mqttPort = 1883

client = mqtt.Client(client_id="pcClient")

client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

client.connect(host = mqttHost, port = mqttPort, keepalive = 10)

client.loop_start()

while True:
    if napedConnected:
        mqttSequence = input()
        if mqttSequence == "S1" or mqttSequence == "s1":
            lol.sequenceTypeOne(client)
        
        if mqttSequence == "S2" or mqttSequence == "s2":
            lol.sequenceTypeTwo(client)
        
        if mqttSequence == "S3" or mqttSequence == "s3":
            lol.sequenceTypeThree(client)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    else:
        print("Napęd nie jest podłączony!")
        time.sleep(5)
