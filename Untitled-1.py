##Test mouvement
import tkinter as tk


class fen():
    def __init__(self):
        self.main_haut = 1600                    
        self.main_larg = 900
        self.canvas = ""
        self.canvas_haut = 1280                     
        self.canvas_larg = 700
        self.score = 0    
        self.score_label = ""
        self.x0=100
        self.dx=5
        self.y0=200

        #self.rect=tk.Canvas.create_rectangle(self.x0,self.x0+20,width=2,fill="red")
        #self
        #self.AfficherFenetre()

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
        jouer=tk.Button(text="Jouer",command=self.deplacer)
        jouer.pack()
        self.rect=self.canvas.create_rectangle(self.x0,self.y0,self.x0+20,self.y0+20,width=2,fill='red')
        tk.mainloop()
    def quitter(self):
        
        self.canvas.delete()     
        self.main.destroy()         
        exit()  
    def deplacer(self):
        print('là')
        self.x0=self.x0+self.dx
        while self.x0>0 or self.x0<self.canvas_haut:
            print('ici')
            self.dx=-self.dx
            self.canvas.coords(self.rect,self.x0,self.y0,self.x0+20,self.y0+20)
        self.canvas.after(50,self.deplacer)
        return     
        exit()
    def rejouer(self):
        self.main.destroy()
        self.__init__()
        self.AfficherFenetre()
    def creevaisseau(self):
        self.haut=vs.ymax-vs.ymin
        self.larg=vs.larg
        self.vaisseau = self.canvas.create_rectangle(self.haut,self.larg)
    

MW = fen()
MW.AfficherFenetre()





