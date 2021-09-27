mport paho.mqtt.client as mqtt
import time
from hal import temperature, humidity, heater
from definitions import user, password, client_id, server, port


# device 1
def message(client, user, msg):
    vetor = msg.payload.decode().split(',')
    heater('on' if vetor[1] == '1' else 'off')
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor[0]}')
    print(vetor)

#
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = message
client.subscribe(f'v1/{user}/things/{client_id}/cmd/2')
client.loop_start()

while True:
    client.publish('v1/'+user+'/things/'+client_id+'/data/0', temperature())
    client.publish('v1/'+user+'/things/'+client_id+'/data/1', humidity())
    time.sleep(10)

# client.disconnect()