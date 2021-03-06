
class projectile():
    def __init__(self,canvas_len, canvas_largeur, objet_x, objet_y, tir_ami,color):
        self.canvas_len = canvas_len                          #On recupere la longueur du canvas
        self.canvas_largeur = canvas_largeur                          #On recupere la hauteur du canvas

        self.tir_ami = tir_ami                                #True = Tir ami

        self.etat = True

        self.largeur = 6                                      #On definit la largeur du projectile
        self.longueur = 10                                     #On definit la longeur du projectile
        self.color = color                                   #On definit la couleur du projectile

        self.deplacer_vit = 4                                 #Vitesse de deplacment du missile

        if self.tir_ami:
            #Si c'est un tir ami, le projectile devra partir du bas du vaisseau et monter
            self.x1 = objet_x - self.largeur/2
            self.y1 = objet_y - self.longueur
            self.x2 = objet_x + self.largeur/2
            self.y2 = objet_y
        else:
            #Si c'est un tir enemeis, le projectile devra partir du bas du vaisseau et monter
            self.x1 = objet_x - self.largeur/2
            self.y1 = objet_y
            self.x2 = objet_x + self.largeur/2
            self.y2 = objet_y + self.longueur

   

    def GetPoints(self):
        return [(self.x1,self.y1),(self.x2,self.y2)]

  
    
    def GetEtat(self):
        return self.etat
    
    def GetEkip(self):
        return self.tir_ami
    
    def Detruire(self):
        self.etat = False
    
    def ModifierCoord(self):
        """Permet de modifier les coordonnes du projectile"""

        if self.tir_ami:
            if 0 < (self.y1 - self.deplacer_vit):
                self.DeplacerHaut()
            else:
                self.etat = False
        else:
            if int(self.canvas_largeur) > (self.y2 + self.deplacer_vit):
                self.DeplacerBas()
            else:
                self.etat = False

    def DeplacerHaut(self):
        self.y1 += - self.deplacer_vit
        self.y2 += - self.deplacer_vit
    
    def DeplacerBas(self):
        self.y1 += + self.deplacer_vit
        self.y2 += + self.deplacer_vit
    
    def CalculerCentre(self):
        return (self.x1 + (self.x2 - self.x1)/2) , (self.y1 + (self.y2 - self.y1)/2)

    
