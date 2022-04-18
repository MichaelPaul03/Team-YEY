from tkinter import *

win = Tk()
win.geometry("307x135+20+20")
win.title("Major Subjects")

list = Listbox(win, selectmode= "single", height=6, width=23)
major = ("reading", "writing", "arithmetic", "coding")

for sub in major:
    list.insert(END, sub)

list.place(x=80, y=15)

win.mainloop()