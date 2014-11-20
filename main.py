##      ##
## TRAP ##
##      ##

from Tkinter import *
import tserver
import tclient
#from PIL import Image, ImageTK

root = Tk()
drawpd =Canvas(root, width=800,height=600, background='white')
class Trap(object):
    def __init__(self, parent):
        self.parent = parent  
        self.container = Frame(parent)
        self.container.pack()
        
game = Trap(root)
root.mainloop()