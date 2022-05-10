from tkinter import *

window = Tk()
window.geometry("462x472")
window.title('Simple Calculator')
window.configure(bg="#b8d0e8")


class MyWindow:
    def __init__(self, window):
        self.lists = []
        self.use = 0

        self.frame = Frame(window, bd=0, width=396, height=100, relief="sunken")
        self.frame.pack(side=TOP)

        self.txtfield = Entry(self.frame, bg="#aedee4", font="sans 20", width=34, bd=30, relief=RIDGE)
        self.txtfield.pack(side=BOTTOM)

        self.frame2 = Frame(window, bd=0, width=396, height=100, relief="sunken")
        self.frame2.pack(side=TOP)

        self.buttonframe = Frame(self.frame2, bg="#aedee4")
        self.buttonframe.pack(side=TOP)

        self.buttonAC = Button(self.buttonframe, text="C", bg="#d9dbdf", font="sans 20 bold", command=lambda: self.clear())
        self.buttonAC.grid(column=0, row=0, pady=3, sticky="nsew", columnspan=4)

        self.button7 = Button(self.buttonframe, text="7", width=6, font="sans 20 bold", command=lambda: self.add("7"))
        self.button7.grid(column=0, row=1, pady=3)

        self.button8 = Button(self.buttonframe, text="8", width=6, font="sans 20 bold", command=lambda: self.add("8"))
        self.button8.grid(column=1, row=1)

        self.button9 = Button(self.buttonframe, text="9", width=6, font="sans 20 bold", command=lambda: self.add("9"))
        self.button9.grid(column=2, row=1)

        self.buttonDiv = Button(self.buttonframe, text="/", bg="#d9dbdf", width=6, font="sans 20 bold", command=lambda: self.add("/"))
        self.buttonDiv.grid(column=3, row=1)

        self.button4 = Button(self.buttonframe, text="4", width=6, font="sans 20 bold", command=lambda: self.add("4"))
        self.button4.grid(column=0, row=2, pady=3)

        self.button5 = Button(self.buttonframe, text="5", width=6, font="sans 20 bold", command=lambda: self.add("5"))
        self.button5.grid(column=1, row=2)

        self.button6 = Button(self.buttonframe, text="6", width=6, font="sans 20 bold", command=lambda: self.add("6"))
        self.button6.grid(column=2, row=2)

        self.buttonMul = Button(self.buttonframe, text="x", bg="#d9dbdf", width=6, font="sans 20 bold", command=lambda: self.add("*"))
        self.buttonMul.grid(column=3, row=2)

        self.button1 = Button(self.buttonframe, text="1", width=6, font="sans 20 bold", command=lambda: self.add("1"))
        self.button1.grid(column=0, row=3, pady=3)

        self.button2 = Button(self.buttonframe, text="2", width=6, font="sans 20 bold", command=lambda: self.add("2"))
        self.button2.grid(column=1, row=3)

        self.button3 = Button(self.buttonframe, text="3", width=6, font="sans 20 bold", command=lambda: self.add("3"))
        self.button3.grid(column=2, row=3)

        self.buttonSub = Button(self.buttonframe, text="-", bg="#d9dbdf", width=6, font="sans 20 bold", command=lambda: self.add("-"))
        self.buttonSub.grid(column=3, row=3)

        self.frame5 = Frame(window, bd=0, width=396, relief="sunken")
        self.frame5.pack(side=TOP)

        self.buttonframex = Frame(self.frame5, bg="#aedee4")
        self.buttonframex.pack(side=TOP)

        self.button0 = Button(self.buttonframex, text="0", width=8, font="sans 20 bold", command=lambda: self.add("0"))
        self.button0.grid(column=0, row=0, ipadx=1, pady=3)

        self.buttonDot = Button(self.buttonframex, text=".", width=8, font="sans 20 bold", command=lambda: self.add("."))
        self.buttonDot.grid(column=1, row=0, ipadx=3)

        self.buttonAdd = Button(self.buttonframex, text="+", bg="#d9dbdf", font="sans 20 bold", width=8, command=lambda: self.add("+"))
        self.buttonAdd.grid(column=2, row=0, ipadx=1)

        self.buttonEqual = Button(self.buttonframex, bg="#FFFFFF", fg="black", text="=", font="sans 20 bold", command=self.display)
        self.buttonEqual.grid(column=0, row=5, sticky="nsew", columnspan=4, pady=3)

    def add(self, char):
        self.lists.append(str(char))
        self.txtfield.insert(END, char)
        self.use = max(self.use - 1, 0)

    def display(self):
        self.use = min(self.use + 1, 1)
        self.txtfield.delete(0, 'end')

        ls = "".join(elem for elem in self.lists)
        ans = eval(ls)
        self.lists.clear()
        self.lists.append(str(ans))

        if float(ans).is_integer():
            self.txtfield.insert(END, int(ans))

        elif isinstance(ans, float):
            self.txtfield.insert(END, float(ans))

    def clear(self):
        if self.use == 0:
            self.txtfield.delete(self.txtfield.index("end") - 1)
            self.lists.pop()

        elif self.use == 1:
            self.txtfield.delete(0, 'end')
            self.lists.clear()

        self.use = max(self.use - 1, 0)


mywin = MyWindow(window)

window.mainloop()