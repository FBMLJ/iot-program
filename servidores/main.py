import threading
import random
from time import sleep

class Sensor(threading.Thread):
    def __init__(self, id, taxa_de_modificacao=10, minimo=-100,maximo = 100, valor_inicial = 0 , sleep_time = 15):
        super().__init__()
        self.id = id
        self.taxa_de_modificacao = taxa_de_modificacao
        self.minimo = minimo
        self.maximo = maximo
        self.valor_atual = 0
        self.sleep_time = sleep_time

    def _atualiza_valor(self):
        self.valor_atual += 2*(random.random() - 0.5) * self.taxa_de_modificacao
    def atualiza(self):
        self._atualiza_valor()
        if self.minimo > self.valor_atual:
            self.valor_atual += self.taxa_de_modificacao
        elif self.maximo < self.valor_atual:
            self.valor_atual -= self.valor_atual

        print(self.id,self.valor_atual)

    def run(self):
        while(True):
            self.atualiza()
            sleep(self.sleep_time * random.random())
if __name__ == "__main__":
    lista_sensores = []
    for i in range(15):

        lista_sensores.append(Sensor(i))
        lista_sensores[i].start()