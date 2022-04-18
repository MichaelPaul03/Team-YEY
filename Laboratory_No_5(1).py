from tkinter import *

win = Tk()
win.geometry("307x135+20+20")
win.title("Label")

# label widget
lbl = Label(win,text ="Laboratory 5", fg = "Black")
lbl.place(x=112, y=45)

lbl1 = Label(win,text = "Submitted to Mam Sayo", fg = "Black")
lbl1.place(x=85, y=65)

win.mainloop()