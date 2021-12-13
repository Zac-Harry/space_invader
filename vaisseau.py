
import tkinter as tk



class vaisseau():
    def __init__(self,canvas_haut,canvas_larg ):
        self.ymin = int(canvas_haut +1 )
        self.larg = int(canvas_larg/2 -10) 
        self.couleur="blue"
        self.ymax = self.xmin +10 

        