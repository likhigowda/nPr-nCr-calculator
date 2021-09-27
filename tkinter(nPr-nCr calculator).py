from tkinter import *
from math import factorial

def npr(n,r):
    try:
        result = (factorial(n))/(factorial(n-r))
        return str(result)
    except:
        return "Math Error"


def ncr(n,r):
    try:
        result = (factorial(n))/(factorial(n-r) * factorial(r))
        return str(result)
    except:
        return "Math Error"


class MyWindow:
    def __init__(self,win):
        self.lb2 = Label(win,text='n',font=("Calibri", 14))
        self.lb3 = Label(win,text='r',font=("Calibri", 14))
        self.lb4 = Label(win,text='result',font=("Calibri", 14))
        self.t2 = Entry(bd=3)
        self.t3 = Entry(bd=3)
        self.t4 = Entry(bd=3)
        self.b1 = Button(win,text='Permutation',font=("Calibri", 14), command=self.perm)
        self.b2 = Button(win,text='Combination',font=("Calibri", 14), command=self.comb)

        self.lb2.place(x=110, y=95)
        self.t2.place(x=140, y=100)

        self.lb3.place(x=110, y=135)
        self.t3.place(x=140, y=140)

        self.b1.place(x=70, y=200)
        self.b2.place(x=210, y=200)

        self.lb4.place(x=80, y=275)
        self.t4.place(x=140, y=280)

    def perm(self):
        self.t4.delete(0,END)
        n = int(self.t2.get())
        r = int(self.t3.get())
        result = npr(n, r)
        self.t4.insert(0,result)

    def comb(self):
        self.t4.delete(0,END)
        n = int(self.t2.get())
        r = int(self.t3.get())
        result = ncr(n, r)
        self.t4.insert(0,result)


window = Tk()
window.title('nPr-nCr calculator')
window.geometry('400x370')
lb1 = Label(master=window,text='Permutation and Combination \ncalculator',font=("Calibri", 14))
lb1.place(x=85,y=30)
mywin = MyWindow(window)
window.mainloop()