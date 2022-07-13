# Import the library
import tkinter as tk
from tkinter import *
from tkinter import ttk
from fiware import get_all_sensor
from subjanela import NovaJanela

# Create an instance of tkinter

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        
        self.sub_janela = None
        ####canvas
        frame = Frame(self, background='black')
        self.canvas = tk.Canvas(frame, width=700, height=300, bg='white', bd=0)
        frame.pack(side=tk.BOTTOM)
        self.button = tk.Button(self, text="Avaliar itens selecionados",  command=self.button_click, bg="#FFF")
        self.button.pack( ipadx=5,
                            ipady=5,
                        )
        self.canvas.pack(padx=1, pady=1)
        self.canvas.old_coords = None
        self.canvas.bind("<Button-1>", self.canvas_button_down)
        self.canvas.bind("<ButtonRelease-1>", self.canvas_button_release)
        self.canvas.bind("<Motion>", self.move_mouse)
        self.lista_sensor = []
        for sensor in get_all_sensor():
           self.lista_sensor.append(Sensor(sensor, self.canvas))
        
            
        #draw square
        self.isDraw = False
        self.ponto1 = None
        self.ponto2 = None
        self.rect = None

    def button_click(self):
        lista_de_sensores_atuais = []
        for sensor in self.lista_sensor:
            if sensor.marcado:
                lista_de_sensores_atuais.append(sensor)
        if self.sub_janela == None:
            self.sub_janela = NovaJanela(self, lista_de_sensores_atuais)
        else:
            self.sub_janela.update(self, lista_de_sensores_atuais)
    def move_mouse(self,e):
        if self.isDraw:
            self.ponto2 = (e.x,e.y)
            self.canvas.delete(self.rect)
            self.rect = self.canvas.create_rectangle(self.ponto1[0], self.ponto1[1], self.ponto2[0], self.ponto2[1])
            
    def canvas_button_down(self,e):
        self.ponto1 = (e.x, e.y)
        self.ponto2 = None
        self.isDraw = True
        
    
    def canvas_button_release(self, e):
        for i in self.lista_sensor:
            i.eventoMarcado(self.ponto1,self.ponto2)
        self.isDraw = False
        self.ponto1 = None
        self.ponto2 = None
        self.canvas.delete(self.rect)
        
import os 
from Sensor import Sensor
# win.mainloop()
import json
if __name__ == "__main__":
    app = App()
       

    
    app.resizable(False, False)
    app.mainloop()
    # t.start()
    