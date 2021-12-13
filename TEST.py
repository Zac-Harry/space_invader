import tkinter as tk


class fen():
    def __init__(self):
        self.main_haut = "1600"                       
        self.main_larg = "900"
        self.canvas = ""
        self.canvas_haut = "1280"                      
        self.canvas_larg = "700" 
        self.score = 0    
        self.score_label = ""
        self.AfficherFenetre()

def AfficherFenetre(self):
    self.main=tk.Tk()
    self.main.geometry(self.main_haut+"x"+self.main_larg)
    self.canvas = tk.Canvas(self.main, width = self.canvas_haut, height = self.canvas_larg, bg ='black')
    self.canvas.pack()   
    self.score_label=tk.Label(self.main , text="Score : "+ str(self.score) )
    self.score_label.pack(side=tk.RIGHT) 

