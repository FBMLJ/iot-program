import threading
import random
from time import sleep
import json
import requests
from datetime import date, datetime

class Sensor(threading.Thread):
    def __init__(self, id, taxa_de_modificacao=10, minimo=-100,maximo = 100, valor_inicial = 0 , sleep_time = 3):
        super().__init__()
        self.id = id
        self.taxa_de_modificacao = taxa_de_modificacao
        self.minimo = minimo
        self.maximo = maximo
        self.valor_atual = valor_inicial
        self.sleep_time = sleep_time

    def _atualiza_broke(self):
        headers = {'Content-Type': 'text/plain'}


        base_url = "http://localhost:1026/v2/entities/sensor_{}/attrs/".format(self.id)
        requests.put(base_url+"dado_atual/value", str(self.valor_atual) , headers=headers)
        
        resp = requests.get(base_url+"historico/")
        dados = json.loads(resp.text)
       
        
        dados["value"].append({ "dado": self.valor_atual, "tempo": str(datetime.now())})
        
        
        resp = requests.put(base_url+"historico", json=dados)
        

    def _atualiza_valor(self):
        self.valor_atual += 2*(random.random() - 0.5) * self.taxa_de_modificacao

    def atualiza(self):
        self._atualiza_valor()
        if self.minimo > self.valor_atual:
            self.valor_atual += self.taxa_de_modificacao
        elif self.maximo < self.valor_atual:
            self.valor_atual -= self.valor_atual

        # print(self.id,self.valor_atual)
        self._atualiza_broke()

    def run(self):
        while(True):
            self.atualiza()
            sleep(self.sleep_time * random.random())

if __name__ == "__main__":
   
    lista_sensores = []
    for i in range(15):

        lista_sensores.append(Sensor(i))
        lista_sensores[i].start()