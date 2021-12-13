import tkinter as tk
from tkinter.constants import CENTER, LEFT, RIGHT
from typing import Text
fen_princ = tk.Tk()

fen_princ.title("SPACE INVADER")

fen_princ.geometry("600x600")


monCanvas = tk.Canvas(fen_princ, width=500, height=500, bg='ivory')
jouer=tk.Button(fen_princ,text="Jouer",fg="light blue",bg="dark red")
quitter=tk.Button(fen_princ,text="Quitter",fg="light blue",bg="dark red",command=fen_princ.destroy)


monCanvas.pack()
jouer.pack(side=LEFT)
quitter.pack(side=RIGHT)

fen_princ.mainloop()

