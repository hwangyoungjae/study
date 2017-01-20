# -*- encoding:utf8 -*-
# Python version in the development environment 2.7.11
import os
os.chdir(os.path.dirname(__file__))
from Tkinter import *
root = Tk()
def closecallback():
    root.destroy()
Button(root, text="Close", command=closecallback).pack()
root.mainloop()