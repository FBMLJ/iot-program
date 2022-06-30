# Import the library
import tkinter as tk
from tkinter import *

# Create an instance of tkinter

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        

        ####canvas
        frame = Frame(self, background='black')
        self.canvas = tk.Canvas(frame, width=700, height=300, bg='white', bd=0)
        frame.pack(side=tk.BOTTOM)
        self.canvas.pack(padx=1, pady=1)
        self.canvas.old_coords = None
        self.canvas.bind("<Button-1>", self.canvas_button_down)
        self.canvas.bind("<ButtonRelease-1>", self.canvas_button_release)
        self.canvas.bind("<Motion>", self.move_mouse)

        #draw square
        self.isDraw = False
        self.ponto1 = None
        self.ponto2 = None
        self.rect = None

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
        self.isDraw = False
        self.ponto1 = None
        self.ponto2 = None
        self.canvas.delete(self.rect)
        
import threading
# win.mainloop()
if __name__ == "__main__":
    app = App()
    app.resizable(False, False)
    app.mainloop()
    # t.start()
    