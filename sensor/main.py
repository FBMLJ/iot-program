from re import I
import threading
import random
from time import sleep
import json
import requests
from datetime import date, datetime
from fiware_interface.atualizar_sensor import atualizar_valor

class Sensor(threading.Thread):
    def __init__(self, id,taxa_de_modificacao=10, minimo=-100,maximo = 100, valor_inicial = 0 , sleep_time = 3):
        super().__init__()
        self.id = id
        
        self.taxa_de_modificacao = taxa_de_modificacao
        self.minimo = minimo
        self.maximo = maximo
        self.valor_atual = valor_inicial
        self.sleep_time = sleep_time
        self.criar_sensor()
    def criar_sensor(self):
        pass
    def _atualiza(self):
        atualizar_valor(self.id,self.valor_atual)
    def _atualiza_valor(self):
        self.valor_atual += 2*(random.random() - 0.5) * self.taxa_de_modificacao

    def atualiza(self):
        self._atualiza_valor()
        if self.minimo > self.valor_atual:
            self.valor_atual += self.taxa_de_modificacao
        elif self.maximo < self.valor_atual:
            self.valor_atual -= self.valor_atual

        # print(self.id,self.valor_atual)
        self._atualiza()

    def run(self):
        while(True):
            self.atualiza()
            sleep(self.sleep_time * random.random())

if __name__ == "__main__":
    from fiware_interface.criando_servico import criando_servico
    criando_servico()
    lista_sensores = []
    import json
    f = open("sensor/dados.json")
    dados = json.load(f)
    # print(data)
    f.close()
    from fiware_interface.criando_sensor import criando_device
    for i,dado in enumerate(dados):
        id = criando_device(dado['tipo'], dado['id'],dado['x'], dado['y'])
        lista_sensores.append(Sensor(id))
        lista_sensores[i].start()
    # for i in range(10):

    # lista_sensores.append(Sensor(0,))
    # lista_sensores[i].start()