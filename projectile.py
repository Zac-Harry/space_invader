class projectile():
    def __init__(self,canvas_haut,canvas_larg,x_depart,y_depart,color):
        self.canvas_haut = int(canvas_haut)
        self.canvas_larg = int(canvas_larg)
        self.largeur = 6                                     
        self.longueur = 10                                     
        self.color = color                                   
        self.vit = 5
        self.etat = True   
        self.x1=x_depart-self.largeur/2
        self.x2= x_depart + self.largeur/2
        self.y1= y_depart - self.longueur
        self.y2= y_depart
    
    
    def Haut(self):
        self.y1 += + self.vit
        self.y2 += + self.vit   


