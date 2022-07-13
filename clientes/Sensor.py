import requests
import json

RAIO = 10
VERDE = "#00dd00"
LARANJA = "#ff7f00"
class Sensor:
    def __init__(self, obj,canvas) :
        self.x = obj['position_x']['value']
        self.y = obj['position_y']['value']
        self.id = obj['id']
        self.type = obj["type"]
        
        self.centro = (self.x + RAIO, self.y + RAIO)
        self.canvas  = canvas
        self.diametro = 2*RAIO
        self.marcado = False
        self.cor = LARANJA
        self.valor = None
        self.update()
    def get_valor(self):

        url = "http://localhost:1026/v2/entities/{}/".format(self.id)

        payload = ""
        headers = {
            "fiware-service": "openiot",
            "fiware-servicepath": "/"
        }

        response = requests.request("GET", url, data=payload, headers=headers)
        return json.loads(response.text)['valor']['value']
       

    def update(self):
        self.canvas.create_oval(self.x,self.y,self.x+self.diametro,self.y+self.diametro,fill=self.cor,outline="")
    def eventoMarcado(self, ponto1, ponto2):
        
        calculo_x = abs(ponto1[0] - self.centro[0]) + abs(ponto2[0] - self.centro[0])
        calculo_y =  abs(ponto1[1] - self.centro[1]) + abs(ponto2[1] - self.centro[1])
        
        if calculo_x == abs(ponto1[0]-ponto2[0]) and calculo_y ==abs(ponto1[1]-ponto2[1]) :
            self.cor = VERDE
            self.marcado = True
        else:
            self.cor = LARANJA
            self.marcado = False

        self.update()
        