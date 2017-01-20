# -*- encoding:utf8 -*-
# Python version in the development environment 2.7.11
import os
os.chdir(os.path.dirname(__file__))
from Tkinter import *

root = Tk()
WidgetCanvas = Canvas(root,bg='yellow', height=250,width=300)
coord = 10, 50, 240, 210
arc = WidgetCanvas.create_arc(coord, start=0, extent=150, fill='red')

WidgetCanvas.pack()
root.mainloop()