# -*- encoding:utf8 -*-
# Python version in the development environment 2.7.11
import os,sys,time
os.chdir(os.path.dirname(__file__))
from Tkinter import *

class MyApp:
    def __init__(self, parent):
        self.myparent = parent

        #--- mainframe 생성 ---
        self.mainframe = Frame(self.myparent)
        self.mainframe.pack()

        #--- button1 생성 ---
        self.button1 = Button(self.mainframe,
                              text="OK",
                              bg="green",
                              command=self.button1click) #명령어묶기로 메서드를 지정
        self.button1.bind("<Return>", self.button1click_a) #사건묶기로 사건과 메서드를 지정
        self.button1.pack()

    #button1의 명령어묶기에 사용된 함수
    def button1click(self):
        if self.button1['bg'] == 'green':
            self.button1['bg'] = 'yellow'
        else:
            self.button1['bg'] = 'green'

    #button1의 사건묶기에 사용된 함수
    def button1click_a(self, event):
        print event #인자로 받은 event출력
        self.button1click()

if __name__ == '__main__':
    root = Tk()
    myapp = MyApp(root)
    root.mainloop()