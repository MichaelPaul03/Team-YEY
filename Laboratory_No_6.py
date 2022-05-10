from tkinter import *

class Grade:
    def __init__(self, win):
        self.pre = Label(win, text = "Prelim Grade:")
        self.pre.place(x = 25, y = 25)
        self.epre = Entry(bd = 3)
        self.epre.place(x = 140, y = 25)
        self.mid = Label(win, text = "Midterm Grade:")
        self.mid.place(x =25, y = 60)
        self.emid = Entry(bd=3)
        self.emid.place(x = 140, y = 60)
        self.fin = Label(win, text = "Final Grade:")
        self.fin.place(x =25, y = 95)
        self.efin = Entry(bd=3)
        self.efin.place(x = 140, y = 95)
        self.sem = Button(win, text = "Semestral Grade:", command = self.grade)
        self.sem.place(x = 25, y = 140)
        self.esem = Entry(bd=3)
        self.esem.place(x=140, y=140)

    def grade(self):
        self.esem.delete(0, 'end')
        grade1 = int(self.epre.get())
        grade2 = int(self.emid.get())
        grade3 = int(self.efin.get())
        final = (grade1 * .3) + (grade2 * .3) + (grade3 * .4)
        self.esem.insert(END, str(final))

window = Tk()
gui = Grade(window)
window.title("Semestral Grade Calculator")
window.geometry("300x200+10+10")
window.mainloop()