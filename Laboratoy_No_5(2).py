from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.entry = Entry()
        self.entry.insert(END, 'This is where I type my text')
        self.entry.place(x=70, y=20)
        self.entry.place(width=150, height=50)

window = Tk()
mywin = MyWindow(window)
window.title('Text field')
window.geometry("300x100")
window.mainloop()