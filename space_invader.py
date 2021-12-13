from tkinter import *

fen_princ = Tk()

fen_princ.title("SPACE INVADER")

fen_princ.geometry("600x600")

monCanvas = Canvas(fen_princ, width=500, height=500, bg='ivory')

monCanvas.pack()

fen_princ.mainloop()