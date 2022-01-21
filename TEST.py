
import tkinter as tk
from alien import alien
from vaisseau import vaisseau
from projectile import projectile
from block import block
import random


    
class fen():
    def __init__(self):
    
        self.main = ""                                #Definition de la fenetre principale
        self.main_longeur = "1600"                        #longueur de la fenetre
        self.main_largeur = "900"                         #largeur de la fenetre

        #REGLAGES JEU
        self.coeff_aleatoire = 150                    #Regler ici la probabilite qu'un alien tire ex si = 10, l'alien a 1 chance sur 10 de tirer
        self.coeff_joueur = 2                         #Probabilite que le tir se declanche  mieux vaut ne pas y toucher.   
        self.score = 0                                #Definition du score
        self.vies = 3                                 #Definition du nombre de vies
        self.vies_label= ""                           #Definition du label ou est inscrit la vie
        self.score_label = ""

        #CANVAS
        self.canvas = ""                              #Defintion de la variable du canvas
        self.canvas_longeur = "1280"                      #Definition de la longueur du canvas
        self.canvas_largeur = "700"                       #Definition de la hauteur du canvas
    
        #ALIENS 

        self.nombre_aliens = 8                       #Nombre d'aliens par lignes
        self.nb_al_dep = 2*self.nombre_aliens

        #Creation des dictionaires des esprits des aliens
        
        self.aliens_att={}                            #Dictionnaire contennat tout les aliens d'attaque(peuvent tirer)
        self.aliens_def={}                            #Dictionnaire contennat tout les aliens de defense (ne peuvent pas tirer)
        
        #Creation des dictionaires contenant les corps des aliens (corps au sens d'objets canvas)
        self.corps_aliens_att={}
        self.corps_aliens_def={}

        self.proj_suppr = []                          #Les id des projectiles a supprimer
        self.al_att_suppr = []                        #Les id des aliens d'attques a supprimer
        self.al_def_suppr = []                        #Les id des aliens de def a supprimer
        

         #BLOCKS 
        self.nb_blocks = 25
        self.blocks = {}
        self.corps_blocks={}
        self.id_bl_suppr = []
        self.coeff_block_inv = 3                      #Chance que le bloc soit invinsible

        #Hauteur des blocks
        self.block_hei = 50

        #Definit la position y des blocks
        self.y1_bl = int(self.canvas_largeur) - 100 - self.block_hei
        self.y2_bl = int(self.canvas_largeur) - 100
        
                       
        
        #Creation des caracteristiques du vaisseau
        self.vaisseau = vaisseau(self.canvas_longeur,self.canvas_largeur)
        self.corps_vaisseau = ""

        #Dictionaires des projectiles et de leur corps (obj canvas)
        self.projectiles = {}
        self.corps_projectiles = {}
        self.limite_aliens = self.y1_bl 
        #Lancement du programme
        self.AfficherFenetre()

    
    def AfficherFenetre(self):
        """Commande d'affichage de la fentetre"""
        
        self.main =tk.Tk() 
        self.main.geometry(self.main_longeur+"x"+self.main_largeur)       #Definit la geometrie de la fenetre   

        #Ici le canvas
        
        self.canvas = tk.Canvas(self.main, width = self.canvas_longeur, height = self.canvas_largeur , bg ='black')
        self.canvas.pack()
        self.background = tk.PhotoImage(file="fond.png")
        self.canvas.create_image(0, 0, image=self.background, anchor='nw')

        self.GenererAliens()                                                  #Genere les aliens
        self.GenererVaisseau()                                                #Genere le vaisseau
        self.GenererBlocks()

        #Lie les touches du clavier au canvas:

        #Permet de bouger en apuyant sur les fleches
        self.main.bind("<Left>", self.vaisseau.MoveLeft)
        self.main.bind("<Right>", self.vaisseau.MoveRight)


        #Permet de tirer en apuyant sur ESPACE
        self.main.bind("<KeyRelease-space>", self.GenererTirAmi)                  

        #Ici la zone de score
        self.score_label=tk.Label(self.main , text="Score : "+ str(self.score) )
        self.score_label.pack(side=tk.RIGHT)

        #ici la zone de vie
        self.vies_label=tk.Label(self.main , text = "Vies : "+ str(self.vies))
        self.vies_label.pack(side=tk.RIGHT)

        #ici le bouton quitter

        bouton1 = tk.Button(self.main , text='Quitter',command=self.quitter)
        bouton1.pack()

        #Ici le bouton demarer

        bouton2 = tk.Button(self.main , text='Rejouer' , command=self.rejouer)
        bouton2.pack()

        #Permet de deplacer les objets
        

        #permet d'actualiser les positions
        self.deplacer()
        self.main.mainloop()
    
    def deplacer(self):
        """Permet de deplacer les differents objects et de mettre a jour le texte"""
        #

        #Mise a jour du nombre de vies et du score
        nb_aliens = len(self.aliens_att) + len(self.aliens_def)
        self.score = abs(nb_aliens - self.nb_al_dep)*100
        self.vies_label['text'] = "Vies : " + str(self.vies)
        self.score_label['text'] = "Score : " + str(self.score)

        if self.VerifCoord():                                                   #Si les coordonnes sont correctes, alors permet a l'esprit de dicter au corps comment bouger

            self.SupprimerMorts()                                               #Permet de supprimer les objets detruits
            
            #Mettre ici la fonctionn qui permet de modifier les coordonnes
            for id in self.aliens_att.keys():
                self.aliens_att[id].ModifierCoord()
            for id in self.aliens_def.keys():
                self.aliens_def[id].ModifierCoord()


            #Mettre ici les fonctions qui permettent a l'alien de tirer
            for id in self.aliens_att.keys():
                self.random = random.randint(0,self.coeff_aleatoire)        #Genere un nombre aleatoire permettant de savoir si l'alien va tirer
                if self.random == 1:
                    x,y = self.aliens_att[id].CalculerCentre()
                    self.GenererProjectile(False,x,y,'red')


            #Mettre ici la modification de l'objet du canvas
            #_

            #Deplacement des aliens d'attaques

            for id in self.aliens_att.keys():
                self.canvas.coords(self.corps_aliens_att[id],self.aliens_att[id].x1,self.aliens_att[id].y1,self.aliens_att[id].x2,self.aliens_att[id].y2) 
            
            #Deplacement des aaliens de defense
            for id in self.aliens_def.keys():
                self.canvas.coords(self.corps_aliens_def[id],self.aliens_def[id].x1,self.aliens_def[id].y1,self.aliens_def[id].x2,self.aliens_def[id].y2) 

            #Deplacement du vaisseau
            self.canvas.coords(self.corps_vaisseau,self.vaisseau.x1,self.vaisseau.y1,self.vaisseau.x2,self.vaisseau.y2)  
            
            #Deplacement du projectile
            if self.projectiles != {}:
                for id in self.projectiles.keys():
                    self.projectiles[id].ModifierCoord()  #Possible erreur ici due a une mauvaise mise a jour des coordonnes
                    self.canvas.coords(self.corps_projectiles[id],self.projectiles[id].x1,self.projectiles[id].y1,self.projectiles[id].x2,self.projectiles[id].y2)
        
            #Realiser les deplacements
            self.main.after(10, self.deplacer)


    #Mettre ici les fonctions afficher
    #
    def GenererBlocks(self):
    
        '''Genere les blocks de defense'''
        #_

        for i in range(self.nb_blocks):
            posX1 = (int(self.canvas_longeur)/self.nb_blocks)*i
            posX2 = (int(self.canvas_longeur)/self.nb_blocks)*(i+1)

            self.random = random.randint(0,self.coeff_block_inv)        #Genere un nombre aleatoire permettant de savoir si l'alien va tirer
            if self.random == 1:
                invincible = True
                color = '#585e5d'
            else:
                invincible = False
                color = '#9b9b9b'

            block1 = block(posX1,self.y1_bl,posX2,self.y2_bl,invincible,color)
            corps_block = self.canvas.create_rectangle(block1.x1,block1.y1,block1.x2,block1.y2,fill = block1.color_fill)
            
            #Genere l'identite du block
            id_blc = self.GenererId(self.blocks)

            #Ajoute le blocks aux dictionaires
            self.blocks[id_blc] = block1
            self.corps_blocks[id_blc] = corps_block

    def GenererAliens(self):

        '''Genere les aliens de defense et d'attaque'''
        #

        #Etablit les positions de l'axe y ou ils commencent:
        y1_att = 0
        y2_att = 50

        y1_def = 100
        y2_def = 150

        for i in range(self.nombre_aliens):

            #Etablit les limites des cadres dans lequelles les aliens peuvent circuler
            mini = (int(self.canvas_longeur)/self.nombre_aliens)*i
            maxi = (int(self.canvas_longeur)/self.nombre_aliens)*(i+1)

            xinf = mini + (maxi-mini)/3         #Position initiale du point x1
            xsup = mini + ((maxi-mini)*2)/3     #Position intitale du point x2

            #Genere l'esprit de l'alien
            alien_att = alien(self.canvas_longeur,self.canvas_largeur,xinf,y1_att,xsup,y2_att,"black",mini,maxi)
            alien_def = alien(self.canvas_longeur,self.canvas_largeur,xinf,y1_def,xsup,y2_def,"red",mini,maxi)

            #Genere le corps de l'alien
            corps_alien_def = self.canvas.create_rectangle(alien_def.x1,alien_def.y1,alien_def.x2,alien_def.y2, fill = alien_def.color_fill)
            corps_alien_att = self.canvas.create_rectangle(alien_att.x1,alien_att.y1,alien_att.x2,alien_att.y2, fill = alien_att.color_fill)
            
            id_att = self.GenererId(self.aliens_att)
            id_def = self.GenererId(self.aliens_def)

            #Ajoute les differents aliens au dictionnaire des aliens
            self.aliens_def[id_def] = alien_def
            self.aliens_att[id_att] = alien_att

            #Ajoute les corps des differents aliens au dictionnaire des corps d'aliens
            self.corps_aliens_att[id_att] = corps_alien_att
            self.corps_aliens_def[id_def] = corps_alien_def

    def GenererVaisseau(self):
        """Genere le corps du vaisseau"""
        #

        self.corps_vaisseau = self.canvas.create_rectangle(self.vaisseau.x1,self.vaisseau.y1,self.vaisseau.x2,self.vaisseau.y2, fill=self.vaisseau.color_fill)
    

    def GenererProjectile(self,tir_ami,x,y,color):
        """Genere les differentes composantes d'un projectile"""
        #_

        #Genere un projectile sur le canvas
        projectile1 = projectile(self.canvas_longeur,self.canvas_largeur,x,y, tir_ami,color)
        corps_projectile = self.canvas.create_rectangle(projectile1.x1,projectile1.y1,projectile1.x2,projectile1.y2, fill=projectile1.color)
        
        id_proj = self.GenererId(self.projectiles)                                            #Genere l'id du projectile
        
        self.projectiles[id_proj] = projectile1                                               #Ajoute l'esprit du projectile
        
        self.corps_projectiles[id_proj] = corps_projectile   #Ajoute les corps du projectile
    
    def GenererTirAmi(self,event):
        """Evenement ou il y a un projetile amis"""
        #Permet de faire du son si on le souhaite quand la personne tire
        
 
        x,y = self.vaisseau.GetCentre()
        self.GenererProjectile(True,x,y,'green')

    

    #Mettre ici les fonction creant l'indentite de l'objet
    #_

    def GenererId(self, dictionaire):

        """Genere une identite pour les projectiles, les aliens"""

        Boucle = True

        while Boucle:
            rand = random.randint(0,1000000)
            if rand not in dictionaire.keys():
                Boucle = False
                return rand

    #Mettre ici les fonction detruisant les objets
    #_


    def SupprimerProjectile(self,identite):
        self.canvas.delete(self.corps_projectiles[identite])        #On supprime d'abord le coprs du projectile de la carte
        self.corps_projectiles.pop(identite)                          #On supprime ensuite son corps du dictionaire des corps
        self.projectiles.pop(identite)                                #On supprime enfin son esprit du dictionaire des esprits
        
        #_AUTRE OPTION_
        #projectile.Detruire()
        #self.canvas.itemconfigure(self.corps_projectiles[i], state = "hidden")

    def SupprimerAlienAtt(self,identite):
        self.canvas.delete(self.corps_aliens_att[identite])
        self.corps_aliens_att.pop(identite)
        self.aliens_att.pop(identite)
    
    def SupprimerAlienDef(self,identite):
        self.canvas.delete(self.corps_aliens_def[identite])
        self.corps_aliens_def.pop(identite)
        self.aliens_def.pop(identite)

    def SupprimerBlock(self,identite):
        self.canvas.delete(self.corps_blocks[identite])
        self.corps_blocks.pop(identite)
        self.blocks.pop(identite)
    
    def SupprimerMorts(self):
        """Permet de supprimer les elements apres la verification de chacun d'entre eux"""
        #_
        #print(self.proj_suppr,self.al_att_suppr,self.al_def_suppr)
        if self.al_att_suppr != []:
            for id_al in self.al_att_suppr:
                self.SupprimerAlienAtt(id_al)
            self.al_att_suppr = []

        if self.al_def_suppr != []:
            for id_al in self.al_def_suppr:
                self.SupprimerAlienDef(id_al)
            self.al_def_suppr = []

        if self.proj_suppr != []:
            for id_proj in self.proj_suppr:
                self.SupprimerProjectile(id_proj)
            self.proj_suppr = []
        
        if self.id_bl_suppr != []:
            for id_bl in self.id_bl_suppr:
                self.SupprimerBlock(id_bl)
            self.id_bl_suppr = []

    #Fonction de verification des coordonnes: Permet de savoir si c'est perdu
    #

    def VerifCoord(self):
  
        if self.VerifGagne():                                       #Si on detruit tout les aliens on arrete le jeu
            self.canvas.create_text(int(self.canvas_longeur)/2,int(self.canvas_largeur)/2,fill="gold",font="Times 100 italic bold",text="Winner")
            return False

        elif self.VerifPositionAlien():                                 
            self.canvas.create_text(int(self.canvas_longeur)/2,int(self.canvas_largeur)/2,fill="red",font="Times 100 italic bold",text="PERDU")
            return False

        elif self.projectiles != {}:
            for id in self.projectiles.keys():                                                #Appelle les identites de tous les projectiles
                if self.projectiles[id].GetEtat():                                            #Si le projectile n'est pas sorti de la fenetre
                    x,y = self.projectiles[id].CalculerCentre()

                    if self.projectiles[id].GetEkip():                                        #Si le projectile est un tir ami

                        for id_al in self.aliens_att.keys():                                  #Verifie si le tir touche un alien de defense
                            if self.aliens_att[id_al].IsColliding(self.projectiles[id].GetPoints()):
                                if id_al not in self.al_att_suppr:
                                    self.al_att_suppr.append(id_al)     
                                if id not in self.proj_suppr:
                                    self.proj_suppr.append(id) 
                        
                        for id_al in self.aliens_def.keys():                                 #Verifie si le tir touche un alien de defense
                            if self.aliens_def[id_al].IsColliding(self.projectiles[id].GetPoints()):
                                if id_al not in self.al_def_suppr:
                                    self.al_def_suppr.append(id_al)
                                if id not in self.proj_suppr:
                                    self.proj_suppr.append(id) 

                    else:                                                                       #Sinon le tir est ennemis

                        for id_bl in self.blocks.keys():
                            
                            if self.blocks[id_bl].IsColliding(self.projectiles[id].GetPoints()):
                                if not self.blocks[id_bl].IsInvincible():
                                    if id_bl not in self.id_bl_suppr:
                                        self.id_bl_suppr.append(id_bl)
                                if id not in self.proj_suppr:
                                    self.proj_suppr.append(id) 
                        
                        #Verifie si le vaisseau est touche par un projectile
                        if self.vaisseau.IsColliding(self.projectiles[id].GetPoints()):     #Si est dans la zone du vaisseau
                            if self.vies > 1:                                                 #Si le vaisseau a assez de vies le jeu continue
                                self.vies += -1
                                if id not in self.proj_suppr:
                                    self.proj_suppr.append(id)

                            else:                                                                #Si le vaisseau n'as plus de vie, arreter le jeu et afficher perdu
                                #Ecriture du message perdu
                                self.canvas.create_text(int(self.canvas_longeur)/2,int(self.canvas_largeur)/2,fill="red",font="Times 100 italic bold",text="PERDU")
                                
                                return False                                                     #Arrete le jeu
                else:
                    if id not in self.proj_suppr:
                        self.proj_suppr.append(id)                                            #Si le projectile sort de la fenetre
            return True                                                                         #SI la verfication a ete faite et rien n'est mauvais, alors proceder
        else:
            return True
    
  

    
 

    
    def VerifPositionAlien(self):
        """Permet de savoir si l'alien a depasse la position autorisee"""

        for id_al in self.aliens_att.keys():
            if self.aliens_att[id_al].y2 >= self.limite_aliens:
                return True                                                           #Si un alien depasse la limite return True
        for id_al in self.aliens_def.keys():
            if self.aliens_def[id_al].y2 >= self.limite_aliens:
                return True 
        return False

    
    def VerifGagne(self):
        """Permet de savoir si le joueur a gagne"""

        if self.aliens_att == {} and self.aliens_def == {}:
            return True
        else:
            return False

    def rejouer(self):
        """Permet de relancer une partie"""
        self.main.destroy()
        self.init()
        self.AfficherFenetre()
    
    def quitter(self):
        """Permet de quitter le jeu"""
        self.canvas.delete("all")     #Detruit le canvas
        self.main.destroy()           #Detruit la fenetre
        exit()                          #Detruit la console
MW= fen()
MW.AfficherFenetre()        
