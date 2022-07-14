import enum
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

        self.tabela2 = ttk.Treeview(self.newWindow)
        self.tabela2['columns'] = ("tipo", "media")
        self.tabela2.pack()
        self.update(janela_principal, lista_de_sensores_atuais)
    
    def media(self, lista_de_sensores_atuais):
        tipo = []
        tipo_cont = []
        tipo_sum = []
        for i in lista_de_sensores_atuais:
            if i.type not in tipo:
                tipo.append(i.type)
                tipo_cont.append(1)
                tipo_sum.append(i.valor)
            else:
                id = tipo.index(i.type)
                tipo_cont[id]+= 1
                tipo_sum[id] += i.valor
            
        # print(tipo,tipo_cont,tipo_sum)
        dic = {}
        for id,i in enumerate(tipo):
            # print(i,id)
            dic[i] = tipo_sum[id]/tipo_cont[id]
        # print(dic)
        return dic
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

        medias = self.media(lista_de_sensores_atuais)
        self.tabela2.column("#0", width=0,  stretch=NO)
        self.tabela2.heading("#0",text="",anchor=CENTER)
        self.tabela2.heading("tipo",text="Tipo",anchor=CENTER)
        self.tabela2.heading("media",text="Média",anchor=CENTER)
        interador = 0
        for key, val in medias.items():
            self.tabela2.insert(parent='',index='end',iid=interador,text='',
            values=(key,val))
            interador+=1

        
        
