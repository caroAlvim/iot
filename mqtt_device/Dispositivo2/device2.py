import paho.mqtt.client as mqtt
import time
from hal2 import temperature, humidity, heater
from definitions2 import user, password, client_id, server, port

# https://www.youtube.com/watch?v=VntoU_xM0uU&t=307s

def message(client, userdata, msg):
    vetor = msg.payload.decode().split(',')
    aquecedor('on' if vetor[1] == '1' else 'off')
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor[0]}')
    print(vetor)

def aquecedor(state: str):
    global rele
    if state == 'on':
        print('Aquecedor ON')
        rele = True
    else:
        print('Aquecedor OFF')
        rele = False

# Comportamento do sistema
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = message
client.subscribe(f'v1/{user}/things/{client_id}/cmd/2')
client.loop_start()

rele: bool=False
temp: int = temperature()
hum: int = humidity()

while True:

    if temp < 30:
        aquecedor('on')
    if temp >= 30:
        aquecedor('off')

    if rele:
        temp = temp + 1
    else:
        temp = temp - 1


    client.publish('v1/'+user+'/things/'+client_id+'/data/0', temperature())
    client.publish('v1/'+user+'/things/'+client_id+'/data/1', humidity())
    time.sleep(10)

# client.disconnect()