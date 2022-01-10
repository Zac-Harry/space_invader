
import tkinter as tk




class vaisseau():
    def __init__(self,canvas_haut,canvas_larg ):
        self.canvas_haut = int(canvas_haut)
        self.canvas_larg = int(canvas_larg)
        self.couleur="blue" 
        self.x1 = 550
        self.y1 = self.canvas_larg - 51
        self.x2 = 650
        self.y2 = self.canvas_larg - 1

        self.haut= self.x2 - self.x1
        self.larg = self.y2 - self.y1    
        self.vit_hor = 20
    def droite(self,ok):
        self.x2=self.x2+self.vit_hor
        self.x1=self.x1+self.vit_hor
        ok

