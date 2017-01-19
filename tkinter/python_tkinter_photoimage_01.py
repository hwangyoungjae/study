# -*- encoding:utf8 -*-
# Python version in the development environment 2.7.11
import os
os.chdir(os.path.dirname(__file__))
from Tkinter import *

root = Tk()
img = PhotoImage(file='sample.gif') #PhotoImage객체 생성
Label(root, image=img).pack()
root.mainloop()
