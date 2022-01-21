

import tkinter as tk

class vaisseau():
    def __init__(self, canvas_len, canvas_largeur):
        self.canvas_len = int(canvas_len)  #Recupere la longueur du canvas
        self.canvas_largeur = int(canvas_largeur)  #Recupere la hauteur du canvas

        #Definition du carre a partir de coordonnes des points 1 (Coord x1 y1) et 2 (Coord x2 y2)
        self.x1 = 400
        self.y1 = self.canvas_largeur - 51
        self.x2 = 500
        self.y2 = self.canvas_largeur - 1

        self.len = self.x2 - self.x1
        self.hei = self.y2 - self.y1
        
        self.color_fill = "blue"

        #Vitesse de delacement du vaisseau
        self.vit_hor = 30 #Vitesse de deplacement horitontal
      
    
    def GetCentre(self):
        x,y = self.x1 +((self.x2 - self.x1)/2), self.y1 +((self.y2- self.y1)/2)
        return x,y

    def MoveRight(self,event):
        if self.x2 <=self.canvas_len:
            self.x2=self.x2+self.vit_hor
            self.x1=self.x1+self.vit_hor
        
        pass


    def MoveLeft(self,event):
        if self.x1 >= 0:
            self.x2=self.x2-self.vit_hor
            self.x1=self.x1-self.vit_hor
    
    def IsColliding(self,Points):
        """Fonctionne en utilisant des coordones sous forme de tupples"""

        #Permet de verifier les collisions en prenant chaque coin de l'objet projectile et verifiant si il n'est pas dans le carre de l'objet percute


        point_proj = []

        point_proj.append(Points[0])
        point_proj.append(Points[1])

        P3_proj,P4_proj = self.CalcAllPoints(Points)                #Permet d'obtenir les points restants

        point_proj.append(P3_proj)
        point_proj.append(P4_proj)

        #Boucle principale verifiant si un des points du prjectil est dans l'alien (les ifs sont pour les testes)
        for point in point_proj:
            if float(point[0]) > float(self.x1) and (float(point[0]) < float(self.x2)):
                if float(point[1]) < float(self.y2) and (float(point[1]) > float(self.y1)):
                    return True
        return False

    def CalcAllPoints(self,Points):
        """ Permet de calculer les points restants a partir des points donnes"""
        
        x3 = Points[1][0]
        y3 = Points[0][1]
        x4 = Points[0][0]
        y4 = Points[1][1]

        return (x3,y3),(x4,y4)


        
        
    
   