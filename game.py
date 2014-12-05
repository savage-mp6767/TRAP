from Tkinter import *

root = Tk()

def subt(a,b):
    if a>b:
        return a-b
    else:
        return b-a

class Wall():
    def __init__(self,parent,x,y,w=15,h=15,color='black'):
        self.parent = parent
        self.x = x
        self.y = y 
        self.w = w
        self.h = h
        self.drawpad = self.parent.drawpad
        self.object = self.drawpad.create_rectangle(self.x,self.y,self.x + w,self.y + h,fill=color)
        self.parent.screenbuffer.append(self)
    
    def SetPos(self,x,y):
        self.x = x
        self.y = y
        self.drawpad.move(self.object,x,y)
        
    def SetColor(self,val):
        self.drawpad.itemconfig(self.object,fill=val)

class Game():
    def __init__(self):
        self.drawpad = Canvas(root, width=800,height=600, background='white')
        self.drawpad.grid(row=0, column=1)
        self.drawpad.bind("<Button-1>",self.MousePress)
        self.drawpad.bind("<ButtonRelease-1>",self.MouseUp)
        self.tempbuffer = []
        self.screenbuffer = []
        self.selected = "NONE"
        self.sx = 0
        self.sy = 0
        self.Update()
    
    def MousePress(self,event):
        if self.selected == "NONE":
            for o in self.screenbuffer:
                if event.x > o.x:
                    if event.y > o.y:
                        if event.x < o.x + o.w:
                            if event.y < o.y + o.h:
                                self.selected = o
                                self.selected.SetColor('red')
                                return
                                
            self.sx = event.x
            self.sy = event.y
        else:
            self.selected.SetPos(subt(event.x,self.selected.x),subt(event.y,self.selected.y))
            self.selected.SetColor('black')
            self.selected = "NONE"
        
    def MouseUp(self,event):
        if self.selected == "NONE":
            if self.sx < event.x or self.sy < event.y:
                Wall(self,self.sx,self.sy,subt(event.x,self.sx),subt(event.y,self.sy))
                #self.tempbuffer.pop()
            else:
                Wall(self,event.x,event.y,subt(event.x,self.sx),subt(event.y,self.sy))
                #self.tempbuffer.pop()
        
    def Update(self):
        self.drawpad.after(10,self.Update)

g = Game()
root.mainloop()