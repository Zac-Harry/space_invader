#   CPE Lyon - 3ETI

#   Auteurs : Lucas ROTH | Romain GAUD

#   Date : 1/5/2021

#   Matiere : CS DEV

#   TP : 3

#   Objectif : Creer une classe qui permet de mettre des blocks de defense

class block():
    def __init__(self,posX1,posY1,posX2,posY2,invincible,color):
        self.x1 = posX1
        self.y1 = posY1
        self.x2 = posX2
        self.y2 = posY2

        self.color_fill = color

        self.invincible = invincible


    def IsInvincible(self):
        return self.invincible
    
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