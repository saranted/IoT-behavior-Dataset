import paho.mqtt.client as mqtt
import sys

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("home/bedroom/fan"+str(sys.argv[1])+"/on/state")
    client.subscribe("home/bedroom/fan"+str(sys.argv[1])+"/on/set")
    client.subscribe("home/bedroom/fan"+str(sys.argv[1])+"/oscillation/state")
    client.subscribe("home/bedroom/fan"+str(sys.argv[1])+"/oscillation/set")
    client.subscribe("home/bedroom/fan"+str(sys.argv[1])+"/speed/state")
    client.subscribe("home/bedroom/fan"+str(sys.argv[1])+"/speed/set")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == "home/bedroom/fan"+str(sys.argv[1])+"/on/set":
        print("publishing new set state")
        client.publish("home/bedroom/fan"+str(sys.argv[1])+"/on/state", msg.payload)
    if msg.topic == "home/bedroom/fan"+str(sys.argv[1])+"/oscillation/set":
        print("publishing new oscillation state")
        client.publish("home/bedroom/fan"+str(sys.argv[1])+"/oscillation/state", msg.payload)
    if msg.topic == "home/bedroom/fan"+str(sys.argv[1])+"/speed/set":
        print("publishing new speed state")
        client.publish("home/bedroom/fan"+str(sys.argv[1])+"/speed/state", msg.payload)

client = mqtt.Client("client-2"+str(sys.argv[1]))
client.connect("192.168.10.100")

client.on_connect = on_connect
client.on_message = on_message


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

