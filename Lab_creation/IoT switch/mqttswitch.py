import paho.mqtt.client as mqtt
import sys

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("home/bedroom/switchmqt"+str(sys.argv[1]))
    client.subscribe("home/bedroom/switchmqt"+str(sys.argv[1])+"/set")
    client.publish("home/bedroom/switchmqt"+str(sys.argv[1])+"/available","ON")
    client.publish("home/bedroom/switchmqt"+str(sys.argv[1]), "ON")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == "home/bedroom/switchmqt"+str(sys.argv[1])+"/set":
        print("publishing new state")
        client.publish("home/bedroom/switchmqt"+str(sys.argv[1]), msg.payload)

client = mqtt.Client("client-100"+str(sys.argv[1]))
client.connect("192.168.10.100")

client.on_connect = on_connect
client.on_message = on_message


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

