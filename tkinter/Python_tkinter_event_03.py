# -*- encoding:utf8 -*-
# Python version in the development environment 2.7.11
from Tkinter import *

class curry: #함수 내포 기법에 사용할 클래스
    def __init__(self, func, *args, **kwargs):
        self.func = func  #함수
        self.pending = args[:] #인자
        self.kwargs = kwargs.copy() #사전형 인자

    def __call__(self, *args, **kwargs):
        if kwargs and self.kwargs:
            kw = self.kwargs.copy()
            kw.update(kwargs)
        else:
            kw = kwargs or self.kwargs
        return self.func(*(self.pending+args), **kw)

class MyApp:
    def __init__(self, parent):
        self.myparent = parent
        #--- mainframe 생성 ---
        self.mainframe = Frame(self.myparent)
        self.mainframe.pack()
        #--- button1생성 ---
        self.button1 = Button(self.mainframe,
                              text='Button1',
                              command=curry(self.buttonclick,"button1click"))
        self.button1.pack()
        #--- button2생성---
        self.button2 = Button(self.mainframe,
                              text='Button2',
                              command=curry(self.buttonclick,"button2click"))
        self.button2.pack()
        #--- button3생성---
        self.button2=Button(self.mainframe,
                            text='Button2',
                            command=curry(self.buttonclick,"button3click"))
        self.button2.pack()
        #--- button4생성---
        self.button2=Button(self.mainframe,
                            text='Button2',
                            command=curry(self.buttonclick,"button4click"))
        self.button2.pack()

    def buttonclick(self,text):
        print(text)

if __name__ == '__main__':
    root=Tk()
    myapp=MyApp(root)
    root.mainloop()