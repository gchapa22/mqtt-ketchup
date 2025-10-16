import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

client = paho.Client(client_id="IoT_Ketchup", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("some_user", "some_Password1")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("9bb1889fece44537aa25fa646c2c152b.s1.eu.hivemq.cloud", 8883)

client.subscribe("trigonometry/#", qos=1)

client.loop_forever()