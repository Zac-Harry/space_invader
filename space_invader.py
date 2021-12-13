import tkinter as Tk

fen_princ = Tk.Tk()

fen_princ.title("SPACE INVADER")

fen_princ.geometry("1000x1000")

monCanvas = Tk.Canvas(fen_princ, width=600, height=600, bg='ivory')

monCanvas.pack()

fen_princ.mainloop()
score=100
scoreLabel = Tk.Label(fen_princ, textvariable = score)
scoreLabel.pack()
