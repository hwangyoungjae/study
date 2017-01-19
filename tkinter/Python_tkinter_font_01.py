# -*- encoding:utf8 -*-
# Python version in the development environment 2.7.11
from Tkinter import *
import tkFont
class APP:
    def __init__(self,root):
        self.myroot=root
        #---font객체생성---
        fontobject = tkFont.Font(root,family='Courier',
                             size=15,
                             weight='bold',
                             slant='italic',
                             underline=True,
                             overstrike=True)
        #---font객체를 적용할 Label생성---
        self.WidgetLabel=Label(root,text="Hello Python")
        self.WidgetLabel['font']=fontobject #font parameter에 font객체적용
        self.WidgetLabel.pack()
root = Tk()
app = APP(root)
root.mainloop()
