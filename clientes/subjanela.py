import tkinter as tk
from tkinter import *
from tkinter import ttk
class NovaJanela:
    def __init__(self,janela_principal, lista_de_sensores_atuais):
        self.pai = janela_principal
        self.newWindow = Toplevel(janela_principal )
        self.newWindow.resizable(True,True)
        self.newWindow.title("Analisando objetos selecionados")
        self.tabela = ttk.Treeview(self.newWindow)
        self.tabela['columns'] = ('id', 'pos_x', 'pos_y', 'valor', 'tipo')
        self.tabela.pack()
        self.update(janela_principal, lista_de_sensores_atuais)
    

    def update(self,janela_principal, lista_de_sensores_atuais):
        
        
        for row in self.tabela.get_children():
            self.tabela.delete(row)
        
        
        
        self.tabela.column("#0", width=0,  stretch=NO)
        self.tabela.column("id",anchor=CENTER, width=250)
        self.tabela.column("pos_x",anchor=CENTER,width=200)
        self.tabela.column("pos_y",anchor=CENTER,width=200)
        self.tabela.column("valor",anchor=CENTER,width=200)
        self.tabela.column("tipo",anchor=CENTER,width=200)

        self.tabela.heading("#0",text="",anchor=CENTER)
        self.tabela.heading("id",text="Id",anchor=CENTER)
        self.tabela.heading("pos_x",text="x",anchor=CENTER)
        self.tabela.heading("pos_y",text="y",anchor=CENTER)
        self.tabela.heading("valor",text="valor",anchor=CENTER)
        self.tabela.heading("tipo",text="tipo",anchor=CENTER)
        
        for i,sensor in enumerate(lista_de_sensores_atuais):
            self.tabela.insert(parent='',index='end',iid=i,text='',
            values=(sensor.id,sensor.x,sensor.y, sensor.get_valor(), sensor.type ))
        
