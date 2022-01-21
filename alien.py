

import tkinter as tk

class alien():
    def __init__(self, canvas_len,canvas_largeur,posX1,posY1,posX2,posY2,color,min,max):
        self.canvas_len = canvas_len  #Recupere la longueur du canvas
        self.canvas_largeur = canvas_largeur  #Recupere la hauteur du canvas

        self.min=min  #Créer le min de la zone où se situe l'alien
        self.max=max  #Créer le max de la zone où se situe l'alien

        #Corps de l'alien
        self.corps_alien = ""

        #Definition du carre a partir de coordonnes des points 1 (Coord x1 y1) et 2 (Coord x2 y2)
        self.x1 = posX1
        self.y1 = posY1
        self.x2 = posX2
        self.y2 = posY2

        #LA couleur
        self.color_fill = color

        #Deplacement de l'alien
        self.positif = True
        self.vit_deplacer_hor = 1 #Vitesse de deplacement horizontal
        self.vit_deplacer_ver = 15 #Vitesse de deplacement vertical

        self.etat = True


    
    def Detruire(self):
        self.etat = False

    def ModifierCoord(self):
        if self.positif:
            if int(self.max) > (self.x2 + self.vit_deplacer_hor):
                self.DeplacerDroit()
            else:
                self.positif = False
                self.DeplacerGauche()
        else:
            if self.min < (self.x1 - self.vit_deplacer_hor):
                self.DeplacerGauche()
            else:
                self.positif = True
                self.DeplacerDroit()
                if int(self.canvas_largeur) > (self.y2 + self.vit_deplacer_ver):
                    self.DeplacerBas()
            
    def DeplacerDroit(self):
        self.x1 += self.vit_deplacer_hor
        self.x2 += self.vit_deplacer_hor
    
    def DeplacerGauche(self):
        self.x1 += - self.vit_deplacer_hor
        self.x2 += - self.vit_deplacer_hor
    
    def DeplacerBas(self):
        self.y1 += self.vit_deplacer_ver
        self.y2 += self.vit_deplacer_ver

    def CalculerCentre(self):
        return (self.x1 + (self.x2 - self.x1)/2) , (self.y1 + (self.y2 - self.y1)/2)

    #LEs prochaines fonctions vont etablir si il ya collision ou non
    def IsColliding(self,Points):
        """Fonctionne en utilisant des coordones sous forme de tupples"""

        #Permet de verifier les collisions en prenant chaque coin de l'objet projectile et verifiant si il n'est pas dans le carre de l'objet percute

        point_proj = []

        point_proj.append(Points[0])
        point_proj.append(Points[1])

        P3_proj,P4_proj = self.CalcAllPoints(Points)

        point_proj.append(P3_proj)
        point_proj.append(P4_proj)

        #Boucle principale verifiant si un des points du prjectil est dans l'alien (les ifs sont pour les testes)
        for point in point_proj:
            if float(point[0]) > float(self.x1) and (float(point[0]) < float(self.x2)):
                    if float(point[1]) < float(self.y2) and (float(point[1]) > float(self.y1)):
                        return True
        return False

    def CalcAllPoints(self,Points):

        x3 = Points[1][0]
        y3 = Points[0][1]
        x4 = Points[0][0]
        y4 = Points[1][1]

        return (x3,y3),(x4,y4)