## hal = hardware abstraction layer 
import random

def temperature():
    return random.randrange(2, 32)


def humidity():
    return random.randrange(10, 95)


def heater (state: str):
    if state == 'on':
        print('aquecedor LIGADO')
    else:
        print('aquecedor DESLIGADO')