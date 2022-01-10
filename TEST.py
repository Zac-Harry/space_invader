import tkinter as tk
from vaisseau import vaisseau

class fen():
    def __init__(self):
        self.main_haut = 1600                       
        self.main_larg = 900
        self.canvas = ""
        self.canvas_haut = 1280                      
        self.canvas_larg = 700
        self.score = 0    
        self.score_label = ""
        self.vaisseau = vaisseau(self.canvas_haut,self.canvas_larg)
        self.corps_vaisseau = ""
        self.AfficherFenetre()
        self.block=block(posX1=10,posY1=10,posX2=20,posY2=20)

    

    def AfficherFenetre(self):
        self.main=tk.Tk()
        self.main.geometry(str(self.main_haut)+"x"+str(self.main_larg))
        self.canvas = tk.Canvas(self.main, width = self.canvas_haut, height = self.canvas_larg, bg ='black')
        self.canvas.pack()   
        self.score_label=tk.Label(self.main , text="Score : "+ str(self.score) )
        self.score_label.pack(side=tk.RIGHT) 
        boutonQuit = tk.Button(self.main , text='Quitter',command=self.quitter)
        boutonQuit.pack()
        self.background = tk.PhotoImage(file="fond.png")
        self.canvas.create_image(0, 0, image=self.background, anchor='nw')
        boutonPA = tk.Button(self.main , text='Rejouer' , command=self.rejouer)
        boutonPA.pack()
        self.creevaisseau()
        self.main.bind("<Left>", self.vaisseau.gauche)
        self.main.bind("<Right>", self.vaisseau.droite)
        self.deplacer()
        
        tk.mainloop()


    def quitter(self):
        
        self.canvas.delete()     
        self.main.destroy()         
        exit()       
    def rejouer(self):
        self.main.destroy()
        self.__init__()
        self.AfficherFenetre()
    def creevaisseau(self):
        self.corps_vaisseau = self.canvas.create_rectangle(self.vaisseau.x1,self.vaisseau.y1,self.vaisseau.x2,self.vaisseau.y2, fill=self.vaisseau.couleur)
    def creeblock(self):
        self.corps_block=self.canvas.create_rectangle(self.block.x1,self.block.y1,self)
    def deplacer(self):
         self.canvas.coords(self.corps_vaisseau,self.vaisseau.x1,self.vaisseau.y1,self.vaisseau.x2,self.vaisseau.y2)
         self.main.after(10, self.deplacer) 
MW = fen()
MW.AfficherFenetre()
