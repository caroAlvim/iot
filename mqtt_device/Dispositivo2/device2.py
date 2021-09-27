import paho.mqtt.client as mqtt
import time
from hal import temperature, humidity, heater
from definitions import user, password, client_id, server, port


# device 2
def message(client, user, msg):
    if msg.topic == 'pucpr/iotmc/carolina/heater':
        heater(msg.payload.decode())

# 
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = message
client.subscribe('pucpr/iotmc/carolina/#')
client.loop_start()

while True:
    client.publish('pucpr/iotmc/carolina/temperature', temperature())
    client.publish('pucpr/iotmc/carolina/humidity', humidity())
    time.sleep(5)

# client.disconnect()
