from tkinter import *

class Window:
    def __init__(self, win):
        self.turn = 0
        self.button = Button(win, text = "Color", bg = "blue", fg = "orange", command=self.colorChange)
        self.button.place(x=50, y=100)
        self.button2 = Button(win, text = "<-- Click this to change the color").place(x=100, y=100)

    def colorChange(self):
        if self.turn == 0:
            self.turn += 1
            self.button.configure(bg = "yellow", fg = "red", activebackground = "blue", activeforeground = "orange")

        elif self.turn == 1:
            self.turn -= 1
            self.button.configure(bg = "blue", fg = "orange", activebackground = "yellow", activeforeground = "red")


tk = Tk()
window = Window(tk)
tk.geometry("300x150")
tk.title("Button")
tk.mainloop()