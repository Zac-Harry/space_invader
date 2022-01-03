
import tkinter as tk



class vaisseau():
    def __init__(self,canvas_haut,canvas_larg ):
        self.haut = int(canvas_haut)
        self.larg = int(canvas_larg) 
        self.couleur="blue" 
        self.__x1 = 400
        self.__y1 = self.larg - 51
        self.__x2 = 500
        self.__y2 = self.larg - 1

        self.__len = self.__x2 - self.__x1
        self.__hei = self.__y2 - self.__y1    

        