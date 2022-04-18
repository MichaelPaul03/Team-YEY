from tkinter import *

window = Tk()
window.title('Father of Computer')
window.geometry("500x200")


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Charles Babbage', background="cyan", foreground="black", font=('Helvetica', 30))
        self.lbl1.place(x=100, y=70)


mywin = MyWindow(window)
window.mainloop()