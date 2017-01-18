# -*- encoding:utf8 -*-
# Python version in the development environment 2.7.11
from Tkinter import *

class MyApp:
    def __init__(self,parent):
        self.myparent=parent
        #--- mainframe 생성 ---
        self.mainframe=Frame(self.myparent)
        self.mainframe.pack()
        #--- button1생성 ---
        self.button1=Button(self.mainframe,
                            text='Button1',
                            command=lambda t="buton1click":self.buttonclick(t))
        self.button1.pack()
        #--- button2생성---
        self.button2=Button(self.mainframe,
                            text='Button2',
                            command=lambda t="buton2click":self.buttonclick(t))
        self.button2.pack()
        #--- button3생성---
        self.button2=Button(self.mainframe,
                            text='Button2',
                            command=lambda t="buton3click":self.buttonclick(t))
        self.button2.pack()
        #--- button4생성---
        self.button2=Button(self.mainframe,
                            text='Button2',
                            command=lambda t="buton4click":self.buttonclick(t))
        self.button2.pack()

    def buttonclick(self,text):
        print(text)

root=Tk()
myapp=MyApp(root)
root.mainloop()