# -*- encoding:utf8 -*-
# Python version in the development environment 2.7.11
from Tkinter import *

class MyApp:
    def __init__(self, parent):
        self.myparent = parent
        #--- mainframe 생성 ---
        self.mainframe=Frame(self.myparent)
        self.mainframe.pack()
        #--- button1생성 ---
        self.button1 = Button(self.mainframe,
                              text='Button1',
                              command=self.button1click) #함수객체
        self.button1.pack()
        #--- button2생성---
        self.button2 = Button(self.mainframe,
                              text='Button2',
                              command=self.button2click()) #함수호출
        self.button2.pack()

    def button1click(self):
        print "button1click"

    def button2click(self):
        print "button2click"

if __name__ == '__main__':
    print '어플리케이션실행'
    root = Tk()
    myapp = MyApp(root)
    root.mainloop()