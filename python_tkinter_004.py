# -*- encoding:utf8 -*-
# Python version in the development environment 2.7.11
import os
os.chdir(os.path.dirname(__file__))
from Tkinter import *

root = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
c1 = Checkbutton(root, text="Music", variable=CheckVar1)
c2 = Checkbutton(root, text="Video", variable=CheckVar2)
c1.pack()
c2.pack()
root.mainloop()
